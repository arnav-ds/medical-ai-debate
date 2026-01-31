import streamlit as st
from conversation import medical_debate

st.set_page_config(page_title="AI Clinical Decision Support System", layout="wide")

st.title(" AI Clinical Decision Support System")

cases = {
    "Sepsis": "Elderly patient, fever, confusion, low BP, tachycardia, suspected infection."
}

selected = st.sidebar.selectbox("Sample Cases", list(cases.keys()))
case_input = st.text_area("Enter Patient Case", cases[selected])

if st.button("Analyze Case"):
    with st.spinner("AI doctors debating..."):
        result = medical_debate(case_input)

    evidence = result["evidence"]
    skeptic = result["skeptic"]
    final = result["final"]

    t1, t2, t3 = st.tabs(["Dr. Evidence", "Dr. Skeptic", "Final Decision"])

    with t1:
        st.markdown("### Diagnosis: " + evidence.get("likely_condition", ""))
        for f in evidence.get("key_findings", []):
            st.markdown(f"- {f}")
        st.markdown("### Initial Management")
        st.write(evidence.get("initial_management", ""))

    with t2:
        st.markdown("### Weakness")
        st.write(skeptic.get("weakness", ""))
        st.markdown("### Missing")
        st.write(skeptic.get("missing", ""))
        st.markdown("### Alternative")
        st.write(skeptic.get("alternative", ""))

    with t3:
        st.markdown("### Final Diagnosis")
        st.write(final.get("final_diagnosis", ""))
        st.markdown("### Immediate Action")
        st.write(final.get("immediate_action", ""))

        conf = final.get("confidence", 0)
        st.progress(conf / 100)
        st.write(f"Confidence: {conf}%")

        for r in final.get("confidence_reasons", []):
            st.markdown(f"- {r}")
