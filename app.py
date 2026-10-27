"""EduPath AI - Home. Run with: streamlit run app.py"""
import streamlit as st
from utils import page_setup, counts, all_topics

page_setup("", "🎓")
st.markdown("# 🎓 EduPath AI")
st.markdown("##### Your personalized study, skill and career companion")

exam = st.session_state.exam
c = counts(exam)
total = len(all_topics(exam))
st.subheader(f"📊 Your progress: {exam}")
m = st.columns(5)
m[0].metric("📚 Topics", total)
m[1].metric("🟢 Mastered", c["Mastered"])
m[2].metric("🟡 In Progress", c["In Progress"])
m[3].metric("🔴 Weak", c["Weak"])
m[4].metric("⚪ Not Started", c["Not Started"])
st.progress(c["Mastered"] / total, text=f"{c['Mastered'] / total:.0%} mastered")

st.subheader("🚀 What would you like to do?")
features = [
    ("📚 Study Planner", "Break your syllabus into topics and track status."),
    ("🗓️ Timetable", "Get a realistic schedule that favours weak topics."),
    ("🤖 AI Tutor", "Simple explanations, key points and practice."),
    ("🎯 Skill Gap", "Compare your skills to a target role."),
    ("🎤 Interview Prep", "Practice questions with instant feedback."),
    ("🧭 Career Guidance", "Find courses and careers that fit you."),
]
for row in (features[:3], features[3:]):
    cols = st.columns(3)
    for col, (t, d) in zip(cols, row):
        col.markdown(f"<div class='card'><h4>{t}</h4>{d}</div>", unsafe_allow_html=True)
    st.write("")
st.info("👈 Pick your exam in the sidebar, then open **Study Planner** from the page menu to begin.")
