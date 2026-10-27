"""Template responses used by the simulated AI tutor. Swap for LLM prompts later."""

EXPLAIN = """**{topic}** is a key part of *{subject}* ({exam}).

1. **Start with the definition**: write {topic} in one sentence of your own.
2. **Learn the 2-3 core rules / formulas / patterns** and when each applies.
3. **Study one solved example** before attempting problems.
4. **Watch for common traps**: most errors come from skipping basics.

🎯 *Tip:* 25 min reading, 25 min solving, 10 min summarising."""

KEY_POINTS = [
    "Define {topic} in one line without looking at notes.",
    "Know where {topic} connects to other topics in {subject}.",
    "Memorise the core formulas/rules, then practise applying them.",
    "Solve at least 5 previous-year questions on {topic}.",
    "Keep a mistake log: write why you got each question wrong.",
]

PRACTICE = [
    ("Easy", "Explain {topic} to a friend in three sentences."),
    ("Easy", "List the key terms/formulas in {topic}."),
    ("Medium", "Solve one previous-year question on {topic}, writing every step."),
    ("Medium", "What are two common mistakes students make in {topic}?"),
    ("Hard", "Create a problem that combines {topic} with another topic from {subject}."),
]

CHAT = {
    "example": "📌 **Example for {topic}:** pick a simple case, solve it step by step, then change one value and see what changes. Want practice questions next?",
    "practice": "📝 Try: (1) define {topic}; (2) solve one PYQ; (3) explain your solution aloud. Open the **Practice** tab for a full set.",
    "why": "🤔 {topic} matters because exam questions often build on it, and it supports later chapters in {subject}.",
    "difference": "⚖️ To compare ideas in {topic}, make a two-column table: definition, formula/usage, example, common mistake.",
    "summary": "🧾 **Quick revision for {topic}:** definition → core rules → one example → common traps. Re-read your mistake log.",
    "default": "💬 Good question on **{topic}**. Break it into: what is given, what is asked, which rule applies. Try asking for an *example*, *practice*, *why* or *summary*.",
}
