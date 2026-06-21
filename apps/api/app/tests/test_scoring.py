from datetime import datetime, timedelta, timezone
from app.models.domain import CompanyProfile, Tender
from app.services.scoring import OpportunityScorer

def test_scoring_rewards_matching_tender() -> None:
    tender = Tender(source="GeM", external_ref="T1", title="AI software platform", buyer_name="Dept", category="software", location="Delhi", estimated_value=1_000_000, published_at=datetime.now(timezone.utc), closes_at=datetime.now(timezone.utc) + timedelta(days=30), portal_url="https://example.com")
    profile = CompanyProfile(company_name="Acme", industries="software,ai", locations="Delhi", annual_turnover=5_000_000)
    score = OpportunityScorer().score(tender, profile)
    assert score["total_score"] >= 90
    assert len(score["reasons"]) == 4
