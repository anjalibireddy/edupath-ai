import streamlit as st
from utils import page_setup, prioritized, explain_topic, key_points, practice_questions, tutor_reply, ICONS

page_setup("AI Tutor", "🤖")
exam = st.session_state.exam
topics = prioritized(exam)  # weak topics come first
labels = [f"{ICONS[s]} {sub}: {t}" for sub, t, s in topics]
choice = st.selectbox("🎯 Choose a topic (weak topics listed first)", range(len(topics)), format_func=lambda i: labels[i])
subject, topic, _ = topics[choice]
tt = (subject, topic)

tab1, tab2, tab3 = st.tabs(["💡 Explanation", "🔑 Key Points", "📝 Practice"])
tab1.markdown(explain_topic(exam, tt))
with tab2:
    for p in key_points(exam, tt):
        st.markdown(f"- ✅ {p}")
with tab3:
    for i, (lvl, q) in enumerate(practice_questions(exam, tt), 1):
        with st.expander(f"Q{i} · {lvl}"):
            st.write(q)
            st.text_area("Your answer", key=f"pq_{topic}_{i}")

st.divider()
st.subheader("💬 Ask a doubt")
if st.button("🧹 Clear chat"):
    st.session_state.chat = []
for role, msg in st.session_state.chat:
    st.chat_message(role).write(msg)
if prompt := st.chat_input(f"Ask about {topic}..."):
    st.session_state.chat.append(("user", prompt))
    st.session_state.chat.append(("assistant", tutor_reply(exam, tt, prompt)))
    st.rerun()
