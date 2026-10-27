"""Shared helpers: state, styling, timetable, tutor, skills, interview feedback, careers."""
import re
from datetime import datetime, timedelta

import pandas as pd
import streamlit as st

import prompts
from data import SYLLABI, ALIASES, CAREERS

STATUSES = ["Not Started", "In Progress", "Mastered", "Weak"]
ICONS = {"Not Started": "⚪", "In Progress": "🟡", "Mastered": "🟢", "Weak": "🔴"}
WEIGHTS = {"Weak": 4, "In Progress": 2, "Not Started": 2, "Mastered": 1}  # study-time weight
START_HOURS = {"🌅 Morning (6 AM)": 6, "☀️ Afternoon (2 PM)": 14, "🌆 Evening (6 PM)": 18, "🌙 Night (9 PM)": 21}

CSS = """<style>
.block-container{padding-top:2rem}
.card{background:#f6f8ff;border:1px solid #dfe5ff;border-radius:14px;padding:1rem 1.2rem;height:100%;color:#1f2a44}
.card h4{margin:0 0 .3rem 0}
</style>"""


# ---------- state & layout ----------
def page_setup(title, icon):
    """Call first on every page: config, state defaults, sidebar exam picker, title."""
    st.set_page_config(page_title=f"{title} · EduPath AI", page_icon=icon, layout="wide")
    defaults = {"exam": list(SYLLABI)[0], "progress": {}, "timetable": None, "chat": [],
                "skills_text": "", "questions": [], "feedback": {}}
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)
    st.markdown(CSS, unsafe_allow_html=True)
    with st.sidebar:
        st.markdown("### 🎓 EduPath AI")
        exams = list(SYLLABI)
        st.session_state.exam = st.selectbox("📘 Exam / Course", exams, index=exams.index(st.session_state.exam))
        st.caption("Data is stored in this browser session only.")
    if title:
        st.title(f"{icon} {title}")


# ---------- syllabus & progress ----------
def key(exam, subject, topic):
    return f"{exam}||{subject}||{topic}"


def get_status(exam, subject, topic):
    return st.session_state.progress.get(key(exam, subject, topic), "Not Started")


def all_topics(exam):
    """[(subject, topic, status)] for an exam."""
    return [(s, t, get_status(exam, s, t)) for s, ts in SYLLABI[exam].items() for t in ts]


def counts(exam):
    c = {s: 0 for s in STATUSES}
    for _, _, stt in all_topics(exam):
        c[stt] += 1
    return c


def prioritized(exam):
    """Weak first, then In Progress, Not Started, Mastered."""
    order = {"Weak": 0, "In Progress": 1, "Not Started": 2, "Mastered": 3}
    return sorted(all_topics(exam), key=lambda x: order[x[2]])


# ---------- timetable ----------
def _row(rows, clock, kind, task, mins):
    end = clock + timedelta(minutes=mins)
    rows.append({"Time": f"{clock:%I:%M %p} - {end:%I:%M %p}", "Type": kind, "Task": task, "Mins": mins})
    return end


def generate_timetable(exam, hours, start_label, days):
    """Weighted round-robin: weak topics appear more often. 50 min study + breaks,
    then revision + flexibility buffer. Returns {day: DataFrame}."""
    topics = prioritized(exam)
    pool = []
    for rep in range(max(WEIGHTS.values())):
        pool += [t for t in topics if WEIGHTS[t[2]] > rep]  # interleaved, not repeated back-to-back
    blocks = max(1, (int(hours * 60) - 45) // 60)  # reserve 30 revision + 15 buffer
    ptr, plan = 0, {}
    for day in days:
        clock, rows = datetime(2000, 1, 1, START_HOURS[start_label]), []
        for i in range(blocks):
            if day == "Sunday" and i == 0:
                clock = _row(rows, clock, "📝 Mock Test", f"Timed practice test for {exam}", 50)
            else:
                s, t, stt = pool[ptr % len(pool)]
                ptr += 1
                clock = _row(rows, clock, "📖 Study", f"{s}: {t} ({stt})", 50)
            if i < blocks - 1:
                long = i % 3 == 2
                clock = _row(rows, clock, "☕ Break", "Long break: walk, snack" if long else "Short break: stretch, water", 20 if long else 10)
        clock = _row(rows, clock, "🔁 Revision", "Revise today's topics + flashcards", 30)
        _row(rows, clock, "🧘 Flex Buffer", "Catch up on unfinished work", 15)
        plan[day] = pd.DataFrame(rows)
    return plan


# ---------- AI tutor (simulated) ----------
def _fmt(text, exam, topic_tuple):
    subject, topic = topic_tuple
    return text.format(topic=topic, subject=subject, exam=exam)


def explain_topic(exam, tt):
    return _fmt(prompts.EXPLAIN, exam, tt)


def key_points(exam, tt):
    return [_fmt(p, exam, tt) for p in prompts.KEY_POINTS]


def practice_questions(exam, tt):
    return [(lvl, _fmt(q, exam, tt)) for lvl, q in prompts.PRACTICE]


def tutor_reply(exam, tt, msg):
    m = msg.lower()
    rules = [("example", ["example", "e.g"]), ("practice", ["practice", "question", "quiz"]),
             ("why", ["why", "important"]), ("difference", ["difference", "compare", " vs "]),
             ("summary", ["summary", "revise", "recap"])]
    for name, words in rules:
        if any(w in m for w in words):
            return _fmt(prompts.CHAT[name], exam, tt)
    return _fmt(prompts.CHAT["default"], exam, tt)


# ---------- skill gap ----------
def extract_skills(text, universe):
    low, found = text.lower(), set()
    for sk in universe:
        names = [sk.lower()] + ALIASES.get(sk, [])
        if any(re.search(rf"(?<![a-z0-9]){re.escape(n)}(?![a-z0-9])", low) for n in names):
            found.add(sk)
    return found


# ---------- interview feedback (rule-based) ----------
def interview_feedback(answer, role_skills):
    words = len(answer.split())
    low = answer.lower()
    good, improve, score = [], [], 0
    if words >= 40: score += 3; good.append("Good depth and length.")
    elif words >= 15: score += 1; improve.append("Add more detail (aim for 40+ words).")
    else: improve.append("Too short: explain your reasoning.")
    if any(w in low for w in ["for example", "project", "built", "used", "implemented"]): score += 2; good.append("You backed it up with an example.")
    else: improve.append("Add a concrete example or project.")
    hits = [s for s in role_skills if s.lower() in low]
    if hits: score += min(3, len(hits)); good.append("Relevant keywords: " + ", ".join(hits[:4]))
    else: improve.append("Use role-specific terminology.")
    if re.search(r"\d", answer): score += 1; good.append("Includes numbers/metrics.")
    if any(w in low for w in ["result", "outcome", "learned", "improved"]): score += 1; good.append("Mentions outcomes.")
    return min(score, 10), good, improve


# ---------- career recommendation ----------
def recommend_careers(interests, score, stage, skills_text):
    results = []
    for c in CAREERS:
        if stage not in c["stage"]:
            continue
        i = len(set(interests) & set(c["interests"])) / len(c["interests"])
        s = min(score / c["min_score"], 1)
        k = len(extract_skills(skills_text, c["skills"])) / len(c["skills"]) if c["skills"] else 0.5
        results.append((round(100 * (0.5 * i + 0.3 * s + 0.2 * k)), c))
    return sorted(results, key=lambda x: -x[0])
