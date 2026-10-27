import random
import streamlit as st
from data import INTERVIEW_QUESTIONS, BEHAVIORAL, ROLES
from utils import page_setup, interview_feedback

page_setup("Interview Prep", "🎤")
a, b, c = st.columns(3)
role = a.selectbox("Role", list(INTERVIEW_QUESTIONS))
level = b.selectbox("Experience", ["Fresher", "Experienced"])
n = c.slider("Questions", 3, 8, 5)

if st.button("🎲 Generate questions", type="primary"):
    pool = INTERVIEW_QUESTIONS[role][level] + BEHAVIORAL
    st.session_state.questions = random.sample(pool, min(n, len(pool)))
    st.session_state.feedback = {}

answers = {}
for i, q in enumerate(st.session_state.questions):
    st.markdown(f"**Q{i + 1}. {q}**")
    answers[i] = st.text_area("Your answer", key=f"ans_{i}", height=100)
    if i in st.session_state.feedback:
        score, good, improve = st.session_state.feedback[i]
        st.progress(score / 10, text=f"Score: {score}/10")
        for g in good: st.success(g)
        for m in improve: st.warning(m)

if st.session_state.questions and st.button("📊 Get feedback"):
    for i, ans in answers.items():
        if ans.strip():
            st.session_state.feedback[i] = interview_feedback(ans, ROLES.get(role, []))
    st.rerun()
if not st.session_state.questions:
    st.info("Choose a role and generate questions to begin.")
