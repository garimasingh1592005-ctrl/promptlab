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

# SCENARIOS (FULL FORMAT 1–5)
scenarios = {

"Scenario 1 — Safety Incident Increase in Night Shift":
"""
Business Insight

Near-miss safety incidents increased by 22% during night shifts in the Raw Materials division over the last 45 days.

⸻

Available Raw Data

* Shift timing
* Incident count
* Overtime hours
* Employee fatigue records
* Supervisor roster
* Safety audit findings

⸻

Business Objective

Leadership wants:

* Root cause analysis
* Preventive actions
* High-risk area identification

⸻

Learner Task

Create an AI prompt using RCTCF framework.
""",

"Scenario 2 — Low Adoption of Digital Tools":
"""
Business Insight

Maintenance teams are not regularly using newly launched digital inspection apps despite training completion.

⸻

Available Raw Data

* App login frequency
* Department-wise usage
* Training attendance records
* Employee age group
* Shift details
* User feedback

⸻

Business Objective

Management wants:

* Adoption barriers
* Engagement strategies
* Improvement roadmap

⸻

Learner Task

Create an AI prompt using available data and business objective.
""",

"Scenario 3 — Decline in Training Engagement":
"""
Business Insight

Mandatory compliance training completion dropped from 92% to 61% among contract workforce employees.

⸻

Available Raw Data

* LMS completion reports
* Department data
* Language preferences
* Attendance records
* Shift schedules
* Mobile usage data

⸻

Business Objective

L&D team wants:

* Root cause analysis
* Engagement strategies
* Completion improvement plan

⸻

Learner Task

Convert business insight into structured AI prompt.
""",

"Scenario 4 — High Downtime in Equipment":
"""
Business Insight

A critical conveyor system experienced repeated downtime during peak operational hours.

⸻

Available Raw Data

* Maintenance logs
* Breakdown frequency
* Equipment age
* Downtime duration
* Spare part replacement history
* Shift-wise production impact

⸻

Business Objective

Operations leadership wants:

* Root cause identification
* Preventive maintenance strategy
* Downtime reduction recommendations

⸻

Learner Task

Build a structured AI prompt for operational analysis.
""",

"Scenario 5 — Employee Engagement Survey Drop":
"""
Business Insight

Employee engagement scores reduced significantly after shift restructuring in one production department.

⸻

Available Raw Data

* Engagement survey scores
* Shift timing changes
* Absenteeism trends
* Employee feedback
* Overtime records
* Attrition data

⸻

Business Objective

HR leadership wants:

* Engagement gap analysis
* Risk prediction
* Corrective intervention plan

⸻

Learner Task

Create a business-focused AI prompt.
"""
}

# SELECT SCENARIO
selected = st.selectbox(
    "Choose Business Scenario",
    list(scenarios.keys())
)

st.info(scenarios[selected])

# USER INPUT
prompt = st.text_area(
    "Write Your AI Prompt (RCTCF Framework)",
    height=300
)

# EVALUATION
if st.button("Evaluate Prompt"):

    score = 0
    feedback = []
    p = prompt.lower()

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
        suggestions.append("- Define AI role clearly")

    if "context:" not in p:
        suggestions.append("- Add business context")

    if "task:" not in p:
        suggestions.append("- Define task clearly")

    if "constraints:" not in p:
        suggestions.append("- Add constraints")

    if "format:" not in p:
        suggestions.append("- Define output format")

    if suggestions:
        for s in suggestions:
            st.write(s)
    else:
        st.success("Prompt is well structured.")

    # PROFESSIONAL SOLUTIONS (AS REQUESTED)
    st.subheader("Professional RCTCF Solution Prompt")

    solutions = {

    "Scenario 1 — Safety Incident Increase in Night Shift":
    """
Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss incidents increased by 22% in night shifts in Raw Materials division.

Task:
Analyze root causes of safety incidents.

Constraints:
Focus on fatigue, supervision gaps, and compliance issues.

Format:
Cause | Risk Impact | Preventive Action | Priority
""",

    "Scenario 2 — Low Adoption of Digital Tools":
    """
Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance teams are not using digital inspection apps.

Task:
Identify adoption barriers and propose improvements.

Constraints:
Consider workforce digital literacy differences.

Format:
Problem | Root Cause | Recommendation | Outcome
""",

    "Scenario 3 — Decline in Training Engagement":
    """
Role:
Act as a Learning & Development Consultant.

Context:
Training completion dropped from 92% to 61%.

Task:
Analyze engagement drop and suggest interventions.

Constraints:
Focus on shift patterns and language barriers.

Format:
Issue | Analysis | Action Plan | Expected Impact
""",

    "Scenario 4 — High Downtime in Equipment":
    """
Role:
Act as a Reliability Engineer.

Context:
Repeated conveyor system downtime affecting production.

Task:
Identify causes and suggest preventive maintenance.

Constraints:
Minimize shutdown time and cost impact.

Format:
Observation | Root Cause | Recommendation | Business Impact
""",

    "Scenario 5 — Employee Engagement Survey Drop":
    """
Role:
Act as an HR Analytics Consultant.

Context:
Engagement dropped after shift restructuring.

Task:
Analyze engagement decline and recommend corrective actions.

Constraints:
Focus on communication and workload balance.

Format:
Issue | Cause | Recommendation | Impact
"""
    }

    st.code(solutions[selected])