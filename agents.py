import json
from llm_provider import ask_llm


def evidence_agent(case):
    prompt = f"""
You are Dr. Evidence.

Return JSON:
{{
  "likely_condition": "",
  "key_findings": ["", "", ""],
  "initial_management": ""
}}

Case:
{case}
"""
    return ask_llm(prompt)


def skeptic_agent(case, evidence):
    prompt = f"""
You are Dr. Skeptic.

Return JSON:
{{
  "weakness": "",
  "missing": "",
  "alternative": ""
}}

Case: {case}
Evidence: {json.dumps(evidence)}
"""
    return ask_llm(prompt)


def final_agent(case, evidence, skeptic):
    prompt = f"""
You are Final Decision Doctor.

Confidence rules:
- <40 if no labs/imaging
- 40–70 if partial evidence
- >70 only if clear criteria

Return JSON:
{{
  "final_diagnosis": "",
  "immediate_action": "",
  "confidence": 0-100,
  "confidence_reasons": ["", "", ""]
}}

Case: {case}
Evidence: {json.dumps(evidence)}
Skeptic: {json.dumps(skeptic)}
"""
    return ask_llm(prompt)
