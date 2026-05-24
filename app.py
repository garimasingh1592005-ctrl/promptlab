import streamlit as st

# PAGE SETTINGS
st.set_page_config(
    page_title="PROMPT LAB",
    layout="wide"
)

# TITLE
st.title("PROMPT LAB")
st.subheader("AI Prompt Quality Evaluator for Tata Steel Professionals")

# FRAMEWORK SECTION
st.markdown("""
## Enterprise Prompting Framework — RCTCF

| Component | Meaning |
|---|---|
| Role | Define AI expertise |
| Context | Explain business situation |
| Task | Define required action |
| Constraints | Specify limitations/focus |
| Format | Define output structure |

Use this framework to create structured enterprise AI prompts.
""")

# SCENARIOS
scenarios = {

    "Scenario 1 — Safety Incident Increase in Night Shift":
    """
    Near-miss safety incidents increased by 22% during night shifts 
    in the Raw Materials division over the last 45 days.

    Teams are concerned about workforce fatigue, reduced supervision,
    and inconsistent compliance during late operational hours.

    Participants must create an AI prompt using the RCTCF framework
    to analyze causes and recommend preventive actions.
    """,

    "Scenario 2 — Low Adoption of Digital Tools":
    """
    Maintenance employees are not regularly using newly launched 
    digital inspection apps despite completing training programs.

    Supervisors report that many employees still prefer manual
    reporting methods during inspections.

    Participants must create an AI prompt using the RCTCF framework
    to identify adoption barriers and improve digital engagement.
    """,

    "Scenario 3 — Decline in Training Engagement":
    """
    Mandatory compliance training completion dropped from 92% to 61%
    within three months among contract workforce employees.

    HR teams suspect low engagement, language barriers,
    and scheduling challenges across shifts.

    Participants must create an AI prompt using the RCTCF framework
    to analyze the issue and suggest practical interventions.
    """,

    "Scenario 4 — High Downtime in Equipment":
    """
    A critical conveyor system experienced repeated downtime during
    peak operational hours, impacting dispatch timelines and productivity.

    Operations teams suspect maintenance gaps, component wear,
    and inconsistent inspection practices.

    Participants must create an AI prompt using the RCTCF framework
    to identify probable causes and preventive improvements.
    """,

    "Scenario 5 — Employee Engagement Survey Drop":
    """
    Employee engagement scores reduced significantly in one production
    department after recent shift restructuring.

    Employees reported communication gaps, workload imbalance,
    and reduced team coordination.

    Participants must create an AI prompt using the RCTCF framework
    to analyze causes and recommend corrective interventions.
    """
}

# DROPDOWN
selected = st.selectbox(
    "Choose Business Scenario",
    list(scenarios.keys())
)

# SHOW SCENARIO
st.info(scenarios[selected])

# USER INPUT
prompt = st.text_area(
    "Write Prompt Using RCTCF Framework",
    height=320,
    placeholder="""
Role:
Act as ...

Context:
Explain the business problem...

Task:
Describe what AI should do...

Constraints:
Mention focus areas, limitations, business conditions...

Format:
Define output structure...
"""
)

# BUTTON
if st.button("Evaluate Prompt"):

    score = 0
    feedback = []

    prompt_lower = prompt.lower()

    # ROLE CHECK
    if "role:" in prompt_lower:
        score += 20
    else:
        feedback.append("❌ Role section missing")

    # CONTEXT CHECK
    if "context:" in prompt_lower:
        score += 20
    else:
        feedback.append("❌ Context section missing")

    # TASK CHECK
    if "task:" in prompt_lower:
        score += 20
    else:
        feedback.append("❌ Task section missing")

    # CONSTRAINT CHECK
    if "constraints:" in prompt_lower:
        score += 20
    else:
        feedback.append("❌ Constraints section missing")

    # FORMAT CHECK
    if "format:" in prompt_lower:
        score += 20
    else:
        feedback.append("❌ Format section missing")

    # SCORE DISPLAY
    st.metric("Prompt Quality Score", f"{score}/100")

    # QUALITY MESSAGE
    if score == 100:
        st.success("Excellent — Prompt follows the RCTCF framework professionally.")
    elif score >= 80:
        st.warning("Good Prompt — Minor improvements needed.")
    elif score >= 60:
        st.warning("Average Prompt — Framework partially followed.")
    else:
        st.error("Weak Prompt Structure — RCTCF framework incomplete.")

    # GAP ANALYSIS
    st.subheader("Gap Analysis")

    if feedback:
        for item in feedback:
            st.write(item)
    else:
        st.success("No major gaps found.")

    # IMPROVEMENT SUGGESTIONS
    st.subheader("Improvement Suggestions")

    suggestions = []

    if "role:" not in prompt_lower:
        suggestions.append("- Add Role section to define AI expertise")

    if "context:" not in prompt_lower:
        suggestions.append("- Add Context section explaining business problem")

    if "task:" not in prompt_lower:
        suggestions.append("- Add Task section describing expected analysis")

    if "constraints:" not in prompt_lower:
        suggestions.append("- Add Constraints section for business focus")

    if "format:" not in prompt_lower:
        suggestions.append("- Add Format section for structured output")

    if suggestions:
        for s in suggestions:
            st.write(s)
    else:
        st.success("Prompt structure is professionally designed.")

    # PROFESSIONAL EXAMPLE
    st.subheader("Professional Prompt Example")

    if selected == "Scenario 6 — Safety Incident Increase in Night Shift":

        example = """
Role:
Act as an Industrial Safety Consultant.

Context:
Near-miss safety incidents increased by 22% during night shifts
in the Raw Materials division over the last 45 days.

Task:
Analyze possible causes behind the increase in incidents
and recommend preventive actions.

Constraints:
Focus on practical shopfloor solutions with low implementation cost
and minimum operational disruption.

Format:
Provide output in:
Cause | Risk Impact | Preventive Action | Priority
"""

    elif selected == "Scenario 7 — Low Adoption of Digital Tools":

        example = """
Role:
Act as a Digital Transformation Consultant.

Context:
Maintenance employees are not regularly using newly launched
digital inspection apps despite completing training programs.

Task:
Identify adoption barriers and recommend strategies
to improve usage and engagement.

Constraints:
Solutions should suit industrial workforce
with varying digital literacy levels.

Format:
Provide output in:
Problem | Root Cause | Recommendation | Expected Outcome
"""

    elif selected == "Scenario 8 — Decline in Training Engagement":

        example = """
Role:
Act as a Learning Engagement Specialist.

Context:
Mandatory compliance training completion dropped from 92% to 61%
in three months among contract workforce employees.

Task:
Analyze reasons for declining completion rates
and suggest engagement interventions.

Constraints:
Recommendations should be practical, multilingual,
and suitable for operational workforce.

Format:
Provide output in:
Issue | Analysis | Suggested Action | Expected Improvement
"""

    elif selected == "Scenario 9 — High Downtime in Equipment":

        example = """
Role:
Act as a Reliability and Maintenance Expert.

Context:
A critical conveyor system experienced repeated downtime
during peak operational hours.

Task:
Identify probable causes of downtime and recommend
preventive maintenance improvements.

Constraints:
Recommendations should minimize shutdown time
and optimize maintenance cost.

Format:
Provide output in:
Observation | Root Cause | Recommendation | Business Impact
"""

    else:

        example = """
Role:
Act as an Employee Engagement Consultant.

Context:
Employee engagement scores reduced significantly
after shift restructuring in one production department.

Task:
Analyze possible reasons for declining engagement
and suggest corrective interventions.

Constraints:
Focus on workforce morale, communication,
and practical implementation.

Format:
Provide output in:
Issue | Possible Cause | Recommendation | Expected Impact
"""

    st.code(example)

# TRAINER DISCUSSION
st.markdown("---")

st.subheader("Trainer Discussion Point")

st.write("""
After reviewing the examples, discuss:

**Why are these prompts better?**
""")

st.write("""
- Business context is clearer
- AI role is defined
- Tasks are actionable
- Constraints improve relevance
- Structured format improves usability
""")

# FINAL MESSAGE
st.success(
    "AI gives generic answers to generic thinking. "
    "Structured prompts create structured business outcomes."
)