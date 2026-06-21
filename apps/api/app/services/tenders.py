import json
from sqlmodel import Session, select
from app.agents.eligibility import EligibilityAgent
from app.models.domain import CompanyProfile, EligibilityReport, ExtractedRequirement, OpportunityScore, Tender
from app.scrapers.demo_portals import CPPPDemoScraper, GeMDemoScraper
from app.services.scoring import OpportunityScorer

class TenderService:
    def __init__(self, session: Session):
        self.session = session

    def ensure_profile(self) -> CompanyProfile:
        profile = self.session.exec(select(CompanyProfile)).first()
        if profile:
            return profile
        profile = CompanyProfile(company_name="Demo AI Solutions Pvt Ltd")
        self.session.add(profile)
        self.session.commit()
        self.session.refresh(profile)
        return profile

    async def scrape_demo_sources(self) -> list[Tender]:
        scraped = []
        for scraper in [GeMDemoScraper(), CPPPDemoScraper()]:
            scraped.extend(await scraper.scrape())
        tenders: list[Tender] = []
        for item in scraped:
            existing = self.session.exec(select(Tender).where(Tender.external_ref == item.external_ref)).first()
            if existing:
                tenders.append(existing)
                continue
            tender = Tender(source=item.source, external_ref=item.external_ref, title=item.title, buyer_name=item.buyer_name, category=item.category, location=item.location, estimated_value=item.estimated_value, published_at=item.published_at, closes_at=item.closes_at, portal_url=item.portal_url, raw_payload=json.dumps(item.raw_payload))
            self.session.add(tender)
            self.session.commit()
            self.session.refresh(tender)
            tenders.append(tender)
        return tenders

    def list_tenders(self) -> list[Tender]:
        return list(self.session.exec(select(Tender).order_by(Tender.closes_at)))

    def score_tender(self, tender_id: int) -> OpportunityScore:
        profile = self.ensure_profile()
        tender = self.session.get(Tender, tender_id)
        if tender is None:
            raise ValueError("Tender not found")
        result = OpportunityScorer().score(tender, profile)
        score = OpportunityScore(tender_id=tender.id, total_score=result["total_score"], industry_score=result["industry_score"], project_size_score=result["project_size_score"], location_score=result["location_score"], timeline_score=result["timeline_score"], reasons=json.dumps(result["reasons"]))
        self.session.add(score)
        self.session.commit()
        self.session.refresh(score)
        return score

    def analyze_tender(self, tender_id: int) -> tuple[EligibilityReport, list[ExtractedRequirement]]:
        profile = self.ensure_profile()
        tender = self.session.get(Tender, tender_id)
        if tender is None:
            raise ValueError("Tender not found")
        result = EligibilityAgent().analyze(tender, profile)
        report = EligibilityReport(tender_id=tender.id, status=result["status"], readiness_score=result["readiness_score"], executive_summary=result["executive_summary"], risks=result["risks"], missing_documents=result["missing_documents"], recommended_next_steps=result["recommended_next_steps"])
        self.session.add(report)
        self.session.commit()
        self.session.refresh(report)
        requirements = []
        for item in result["requirements"]:
            req = ExtractedRequirement(report_id=report.id, **item)
            self.session.add(req)
            requirements.append(req)
        self.session.commit()
        for req in requirements:
            self.session.refresh(req)
        return report, requirements
