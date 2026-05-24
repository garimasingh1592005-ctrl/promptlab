import streamlit as st

st.set_page_config(
    page_title="PROMPT LAB",
    layout="wide"
)

st.title("PROMPT LAB")
st.subheader("AI Prompt Quality Evaluator for Tata Steel Professionals")

# FRAMEWORK
st.markdown("""
## Enterprise Prompting Framework — RCTCF

| Component | Meaning |
|---|---|
| Role | Define AI expertise |
| Context | Business situation |
| Task | What AI should do |
| Constraints | Limits & focus areas |
| Format | Output structure |
""")

# SCENARIOS (clean + neutral + enterprise framing)
scenarios = {

    "Scenario 1 — Safety Incident Increase in Night Shift":
    """
Near-miss safety incidents have increased by 22% during night shifts
in the Raw Materials division over the last 45 days.

Teams have observed fatigue-related errors, reduced supervision coverage,
and inconsistent adherence to safety protocols during late hours.

Focus: Use RCTCF framework
""",

    "Scenario 2 — Low Adoption of Digital Tools":
    """
Maintenance employees are not consistently using newly deployed
digital inspection applications despite formal training completion.

Manual reporting is still preferred in several operational areas,
leading to delayed digitization benefits.

Focus: Use RCTCF framework
""",

    "Scenario 3 — Decline in Training Engagement":
    """
Mandatory compliance training completion has dropped significantly
from 92% to 61% over a three-month period among contract workforce.

Multiple operational shifts and workforce diversity may be impacting participation.

Focus: Use RCTCF framework
""",

    "Scenario 4 — High Downtime in Equipment":
    """
A critical conveyor system has experienced repeated unplanned downtime
during peak production hours, affecting dispatch performance.

Possible contributing factors include maintenance gaps and component reliability issues.

Focus: Use RCTCF framework
""",

    "Scenario 5 — Employee Engagement Survey Drop":
    """
Employee engagement scores have declined in one production department
following recent shift restructuring and workflow changes.

Concerns have been observed around communication flow and workload distribution.

Focus: Use RCTCF framework
"""
}

# SELECT SCENARIO
selected = st.selectbox(
    "Choose Business Scenario",
    list(scenarios.keys())
)

st.info(scenarios[selected])

# INPUT
prompt = st.text_area(
    "Write Prompt Using RCTCF Framework",
    height=300,
    placeholder="""
Role:
Context:
Task:
Constraints:
Format:
"""
)

# EVALUATION
if st.button("Evaluate Prompt"):

    score = 0
    feedback = []
    p = prompt.lower()

    # STRICT STRUCTURE CHECK
    if "role:" in p:
        score += 20
    else:
        feedback.append("❌ Missing Role section")

    if "context:" in p:
        score += 20
    else:
        feedback.append("❌ Missing Context section")

    if "task:" in p:
        score += 20
    else:
        feedback.append("❌ Missing Task section")

    if "constraints:" in p:
        score += 20
    else:
        feedback.append("❌ Missing Constraints section")

    if "format:" in p:
        score += 20
    else:
        feedback.append("❌ Missing Format section")

    st.metric("Prompt Quality Score", f"{score}/100")

    if score == 100:
        st.success("Excellent — Fully RCTCF compliant enterprise prompt.")
    elif score >= 80:
        st.warning("Good prompt — minor improvements needed.")
    else:
        st.error("Weak prompt — incomplete RCTCF structure.")

    st.subheader("Gap Analysis")
    if feedback:
        for f in feedback:
            st.write(f)
    else:
        st.success("No structural gaps detected.")

    st.subheader("Improvement Suggestions")

    suggestions = []

    if "role:" not in p:
        suggestions.append("- Define AI role clearly (e.g., Safety Consultant)")

    if "context:" not in p:
        suggestions.append("- Add business context for better grounding")

    if "task:" not in p:
        suggestions.append("- Clearly define analytical task")

    if "constraints:" not in p:
        suggestions.append("- Add constraints (cost, safety, operations, etc.)")

    if "format:" not in p:
        suggestions.append("- Define structured output format")

    if suggestions:
        for s in suggestions:
            st.write(s)
    else:
        st.success("Prompt is well structured.")

    # PROFESSIONAL EXAMPLE
    st.subheader("Professional Example (RCTCF)")

    examples = {
        "Scenario 1 — Safety Incident Increase in Night Shift": """
Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss incidents increased by 22% in night shifts in Raw Materials division.

Task:
Identify root causes behind incident increase.

Constraints:
Focus on low-cost, practical shopfloor safety interventions.

Format:
Cause | Risk Impact | Preventive Action | Priority
""",

        "Scenario 2 — Low Adoption of Digital Tools": """
Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance teams are not consistently using digital inspection tools.

Task:
Analyze adoption barriers and improvement strategies.

Constraints:
Consider varying digital literacy levels.

Format:
Problem | Root Cause | Recommendation | Outcome
"""
    }

    st.code(examples[selected] if selected in examples else examples["Scenario 1 — Safety Incident Increase in Night Shift"])