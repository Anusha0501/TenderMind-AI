from app.models.domain import CompanyProfile, Tender

class EligibilityAgent:
    """Deterministic demo implementation matching the planned LangGraph nodes."""
    def analyze(self, tender: Tender, profile: CompanyProfile) -> dict[str, object]:
        requirements = [
            {"requirement_type": "turnover", "description": "Bidder should have sufficient annual turnover for the project scale.", "required_value": str((tender.estimated_value or 0) * 1.5), "evidence": "Derived from tender value risk policy for demo readiness analysis.", "decision": "pass" if profile.annual_turnover >= (tender.estimated_value or 0) * 1.5 else "needs_review", "confidence": 0.82},
            {"requirement_type": "certification", "description": "Relevant quality or MSME certification should be available.", "required_value": "ISO 9001 or MSME", "evidence": "Company profile certification comparison.", "decision": "pass" if any(x in profile.certifications.upper() for x in ["ISO", "MSME"]) else "unknown", "confidence": 0.78},
            {"requirement_type": "experience", "description": "Prior experience should match the tender category.", "required_value": tender.category, "evidence": "Tender category compared with experience keywords.", "decision": "pass" if tender.category.split()[0].lower() in profile.experience_keywords.lower() else "needs_review", "confidence": 0.74},
        ]
        readiness = round(sum(100 if r["decision"] == "pass" else 55 for r in requirements) / len(requirements))
        needs_review = any(r["decision"] != "pass" for r in requirements)
        return {"status": "needs_review" if needs_review else "approved", "readiness_score": readiness, "executive_summary": f"{tender.title} is {'ready for human approval' if not needs_review else 'promising but requires review'} with a readiness score of {readiness}.", "risks": "Review ambiguous requirements before bid commitment." if needs_review else "No critical demo risks detected.", "missing_documents": "Upload supporting certificates and past work orders for final validation.", "recommended_next_steps": "Have a tender manager validate extracted criteria and approve the pursuit decision.", "requirements": requirements}
