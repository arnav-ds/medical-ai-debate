from agents import evidence_agent, skeptic_agent, final_agent


def medical_debate(case):
    evidence = evidence_agent(case)
    skeptic = skeptic_agent(case, evidence)
    final = final_agent(case, evidence, skeptic)

    return {
        "evidence": evidence,
        "skeptic": skeptic,
        "final": final,
        "confidence": final.get("confidence", 0),
        "confidence_reasons": final.get("confidence_reasons", [])
    }
