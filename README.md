# 🎓 EduPath AI

Personalized education & career guidance (Streamlit MVP). All "AI" is rule-based/template driven, so **no API keys are needed**.

## Setup
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```
Open http://localhost:8501.

## Structure
- `app.py` – Home dashboard
- `pages/` – Study Planner, Timetable, AI Tutor, Skill Gap, Interview Prep, Career Guidance
- `data.py` – sample syllabi, job roles, interview questions, careers
- `prompts.py` – tutor/response templates
- `utils.py` – shared logic (state, timetable, skill matching, feedback, recommendations)

## Notes
- Data lives in `st.session_state` only: refreshing the browser resets it.
- Resume upload accepts `.txt`; for PDFs paste the text (or add `pypdf`).
- **Plugging in a real LLM later:** replace `tutor_reply`, `explain_topic`, `interview_feedback` and `recommend_careers` in `utils.py`; the pages only call these functions.
- Add exams/roles by editing `data.py`.
