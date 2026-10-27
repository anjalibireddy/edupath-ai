import streamlit as st
from data import SYLLABI
from utils import page_setup, STATUSES, ICONS, key, get_status, counts, all_topics, prioritized

page_setup("Study Planner", "📚")
exam = st.session_state.exam
st.caption(f"Mark each topic's status for **{exam}**. Weak topics get priority everywhere else.")

c, total = counts(exam), len(all_topics(exam))
cols = st.columns(4)
for col, s in zip(cols, STATUSES):
    col.metric(f"{ICONS[s]} {s}", c[s])
st.progress(c["Mastered"] / total, text=f"Overall mastery: {c['Mastered'] / total:.0%}")

left, right = st.columns([2, 1])
with left:
    for subject, topics in SYLLABI[exam].items():
        done = sum(get_status(exam, subject, t) == "Mastered" for t in topics)
        with st.expander(f"{subject}  ·  {done}/{len(topics)} mastered", expanded=True):
            st.progress(done / len(topics))
            for t in topics:
                a, b = st.columns([2, 1])
                a.write(f"{ICONS[get_status(exam, subject, t)]} {t}")
                k = key(exam, subject, t)
                st.session_state.progress[k] = b.selectbox(
                    "Status", STATUSES, index=STATUSES.index(get_status(exam, subject, t)),
                    key=f"sel_{k}", label_visibility="collapsed")
with right:
    st.subheader("🎯 Priority Queue")
    top = [x for x in prioritized(exam) if x[2] in ("Weak", "In Progress")][:8]
    if not top:
        st.info("Mark some topics as Weak or In Progress to build your queue.")
    for s, t, stt in top:
        st.markdown(f"{ICONS[stt]} **{t}** · _{s}_")
