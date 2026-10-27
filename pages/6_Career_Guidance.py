import streamlit as st
from data import INTERESTS, STAGES
from utils import page_setup, recommend_careers

page_setup("Career Guidance", "🧭")
with st.form("career"):
    stage = st.radio("Where are you now?", STAGES, horizontal=True)
    interests = st.multiselect("💛 Your interests", INTERESTS, default=["Coding"])
    score = st.slider("📈 Academic performance (%)", 30, 100, 70)
    skills = st.text_area("🛠️ Current skills (optional)", value=st.session_state.skills_text, height=80)
    go = st.form_submit_button("🔮 Recommend paths", type="primary")

if go:
    if not interests:
        st.warning("Pick at least one interest.")
    for fit, c in recommend_careers(interests, score, stage, skills):
        with st.container(border=True):
            st.markdown(f"### {c['name']}")
            st.progress(fit / 100, text=f"Fit score: {fit}%")
            st.write(c["desc"])
            st.markdown(f"➡️ **Next step:** {c['next']}")
