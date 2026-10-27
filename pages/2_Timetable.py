import streamlit as st
from utils import page_setup, generate_timetable, START_HOURS

page_setup("Smart Timetable", "🗓️")
exam = st.session_state.exam

with st.form("tt"):
    a, b = st.columns(2)
    hours = a.slider("⏱️ Study hours per day", 1.5, 12.0, 4.0, 0.5)
    start = b.selectbox("🕒 Preferred study time", list(START_HOURS))
    days = st.multiselect("📅 Study days", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                          default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
    go = st.form_submit_button("✨ Generate timetable", type="primary")

if go:
    if days:
        st.session_state.timetable = generate_timetable(exam, hours, start, days)
    else:
        st.warning("Select at least one study day.")

plan = st.session_state.timetable
if plan:
    all_rows = [r for df in plan.values() for r in df["Task"]]
    study = [r for r in all_rows if "(" in r and r.endswith(")")]
    weak_share = sum("(Weak)" in r for r in study) / max(len(study), 1)
    m = st.columns(3)
    m[0].metric("📅 Study days", len(plan))
    m[1].metric("📖 Study blocks / week", len(study))
    m[2].metric("🔴 Weak-topic share", f"{weak_share:.0%}")
    st.caption("Tip: Sundays include a mock test. Weak topics appear more often; the buffer slot keeps the plan flexible.")
    tabs = st.tabs(list(plan))
    for tab, (day, df) in zip(tabs, plan.items()):
        with tab:
            st.dataframe(df.drop(columns="Mins"), use_container_width=True, hide_index=True)
            st.download_button("⬇️ Download CSV", df.to_csv(index=False), f"{day}.csv", key=f"dl_{day}")
else:
    st.info("Set your hours and click **Generate timetable**.")
