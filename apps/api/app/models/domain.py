from datetime import datetime, timezone
from enum import Enum
from typing import Optional
from sqlmodel import Field, SQLModel

class TenderStatus(str, Enum):
    open = "open"
    closed = "closed"
    archived = "archived"

class ReviewStatus(str, Enum):
    draft = "draft"
    needs_review = "needs_review"
    approved = "approved"
    rejected = "rejected"

def now_utc() -> datetime:
    return datetime.now(timezone.utc)

class CompanyProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str
    industries: str = "software,cloud,ai"
    locations: str = "Delhi,India,Remote"
    annual_turnover: float = 15_000_000
    certifications: str = "ISO 9001,MSME"
    experience_keywords: str = "software platform,analytics,automation,ai"
    min_project_value: float = 100_000
    max_project_value: float = 50_000_000
    created_at: datetime = Field(default_factory=now_utc)

class Tender(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    source: str
    external_ref: str = Field(index=True)
    title: str
    buyer_name: str
    category: str
    location: str
    estimated_value: float | None = None
    published_at: datetime
    closes_at: datetime
    portal_url: str
    status: TenderStatus = TenderStatus.open
    raw_payload: str = "{}"
    created_at: datetime = Field(default_factory=now_utc)

class OpportunityScore(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tender_id: int = Field(index=True)
    total_score: int
    industry_score: int
    project_size_score: int
    location_score: int
    timeline_score: int
    reasons: str
    created_at: datetime = Field(default_factory=now_utc)

class EligibilityReport(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tender_id: int = Field(index=True)
    status: ReviewStatus = ReviewStatus.needs_review
    readiness_score: int
    executive_summary: str
    risks: str
    missing_documents: str
    recommended_next_steps: str
    created_at: datetime = Field(default_factory=now_utc)

class ExtractedRequirement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    report_id: int = Field(index=True)
    requirement_type: str
    description: str
    required_value: str
    evidence: str
    decision: str
    confidence: float
