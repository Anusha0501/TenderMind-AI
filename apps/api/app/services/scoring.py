from datetime import datetime, timezone
from app.models.domain import CompanyProfile, Tender

class OpportunityScorer:
    def score(self, tender: Tender, profile: CompanyProfile) -> dict[str, object]:
        industries = [item.strip().lower() for item in profile.industries.split(",")]
        locations = [item.strip().lower() for item in profile.locations.split(",")]
        haystack = f"{tender.title} {tender.category}".lower()
        industry_score = 30 if any(item in haystack for item in industries) else 8
        if tender.estimated_value is None:
            project_size_score = 12
        elif profile.min_project_value <= tender.estimated_value <= profile.max_project_value:
            project_size_score = 25
        else:
            project_size_score = 6
        location_score = 20 if any(item in tender.location.lower() for item in locations) else 8
        days_left = max((tender.closes_at - datetime.now(timezone.utc)).days, 0)
        timeline_score = 25 if days_left >= 21 else 16 if days_left >= 10 else 5
        total = industry_score + project_size_score + location_score + timeline_score
        reasons = [
            f"Industry score {industry_score}/30 from category and title match.",
            f"Project size score {project_size_score}/25 against configured value range.",
            f"Location score {location_score}/20 against preferred regions.",
            f"Timeline score {timeline_score}/25 with {days_left} days remaining.",
        ]
        return {"total_score": total, "industry_score": industry_score, "project_size_score": project_size_score, "location_score": location_score, "timeline_score": timeline_score, "reasons": reasons}
