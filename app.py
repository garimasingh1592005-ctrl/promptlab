import streamlit as st

# PAGE SETTINGS
st.set_page_config(
    page_title="PROMPT LAB",
    layout="wide"
)

# TITLE
st.title("PROMPT LAB")
st.subheader("AI Prompt Quality Evaluator for Tata Steel Professionals")

# SCENARIOS
scenarios = {
    "Safety Scenario":
    """
    Blast Furnace incidents increased during B-shift
    despite safety training completion.
    """,

    "Maintenance Scenario":
    """
    Rolling Mill Unit-2 is facing repeated downtime
    despite preventive maintenance.
    """,

    "L&D Scenario":
    """
    Training completion is high but practical skill
    performance remains low among new technicians.
    """,

    "Operations Scenario":
    """
    Shift handover reports are inconsistent across teams.
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
    "Write Your AI Prompt",
    height=200
)

# BUTTON
if st.button("Evaluate Prompt"):

    score = 0
    feedback = []

    # ROLE CHECK
    if "act as" in prompt.lower():
        score += 20
    else:
        feedback.append("❌ Missing Role")

    # CONTEXT CHECK
    if len(prompt.split()) > 20:
        score += 20
    else:
        feedback.append("❌ Weak Context")

    # TASK CHECK
    if any(word in prompt.lower() for word in [
        "analyze",
        "identify",
        "suggest",
        "recommend"
    ]):
        score += 20
    else:
        feedback.append("❌ Task Not Clearly Defined")

    # CONSTRAINT CHECK
    if any(word in prompt.lower() for word in [
        "focus on",
        "consider",
        "constraints"
    ]):
        score += 20
    else:
        feedback.append("❌ Constraints Missing")

    # FORMAT CHECK
    if any(word in prompt.lower() for word in [
        "table",
        "format",
        "bullet",
        "dashboard"
    ]):
        score += 20
    else:
        feedback.append("❌ Output Format Missing")

    # SCORE DISPLAY
    st.metric("Prompt Quality Score", f"{score}/100")

    # QUALITY MESSAGE
    if score >= 80:
        st.success("Excellent Enterprise-Level Prompt")
    elif score >= 60:
        st.warning("Good Prompt — Some Improvements Needed")
    else:
        st.error("Weak Prompt Structure")

    # GAP ANALYSIS
    st.subheader("Gap Analysis")

    if feedback:
        for item in feedback:
            st.write(item)
    else:
        st.success("No Major Gaps Found")

    # IMPROVEMENT SUGGESTIONS
    st.subheader("Improvement Suggestions")

    suggestions = []

    if "act as" not in prompt.lower():
        suggestions.append("- Add professional role definition")

    if len(prompt.split()) < 20:
        suggestions.append("- Add more business context")

    if "focus on" not in prompt.lower():
        suggestions.append("- Add constraints or focus areas")

    if "table" not in prompt.lower():
        suggestions.append("- Define output format clearly")

    if suggestions:
        for s in suggestions:
            st.write(s)
    else:
        st.success("Prompt structure is professionally designed")

    # PROFESSIONAL EXAMPLE
    st.subheader("Professional Prompt Example")

    if selected == "Safety Scenario":
        example = """
Act as Tata Steel Safety Consultant.

Analyze why Blast Furnace incidents increased during B-shift
despite safety training completion.

Focus on:
- workforce fatigue
- supervision quality
- compliance gaps

Present findings in table format
with root causes and corrective actions.
"""

    elif selected == "Maintenance Scenario":
        example = """
Act as Industrial Maintenance Consultant.

Analyze why Rolling Mill Unit-2 is facing repeated downtime
despite preventive maintenance.

Focus on:
- lubrication schedules
- spare part quality
- operator handling

Present recommendations in bullet format.
"""

    elif selected == "L&D Scenario":
        example = """
Act as Workforce Capability Development Specialist.

Analyze why training completion is high
but practical performance remains low.

Focus on:
- practical exposure
- mentoring quality
- assessment gaps

Present findings in dashboard format.
"""

    else:
        example = """
Act as Operations Excellence Consultant.

Analyze why shift handover reports are inconsistent.

Focus on:
- reporting standards
- communication gaps
- shift coordination

Present findings in table format.
"""

    st.code(example)