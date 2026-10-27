import streamlit as st
from data import ROLES, RESOURCES
from utils import page_setup, extract_skills

page_setup("Skill Gap Analyzer", "🎯")
role = st.selectbox("🎓 Target role", list(ROLES))
up = st.file_uploader("📄 Upload resume (.txt)", type=["txt"])
text = st.text_area("Or paste your resume / skills", value=st.session_state.skills_text, height=180)
if up:
    text = up.read().decode("utf-8", errors="ignore")
st.session_state.skills_text = text

if st.button("🔍 Analyze", type="primary"):
    required = ROLES[role]
    have = extract_skills(text, required)
    missing = [s for s in required if s not in have]
    pct = len(have) / len(required)
    st.progress(pct, text=f"Role match: {pct:.0%}")
    a, b = st.columns(2)
    a.metric("✅ Skills you have", len(have))
    b.metric("⚠️ Skills to learn", len(missing))
    a.success(", ".join(sorted(have)) or "No matching skills found yet.")
    st.subheader("📚 Free resources for your gaps")
    if not missing:
        st.balloons()
        st.success("You cover every core skill for this role. Now build projects!")
    for s in missing:
        name, url = RESOURCES.get(s, ("roadmap.sh", "https://roadmap.sh"))
        st.markdown(f"- **{s}** → [{name}]({url})")
