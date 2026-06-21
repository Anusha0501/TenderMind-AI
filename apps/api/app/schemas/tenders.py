from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TenderRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    source: str
    external_ref: str
    title: str
    buyer_name: str
    category: str
    location: str
    estimated_value: float | None
    published_at: datetime
    closes_at: datetime
    portal_url: str
    status: str

class ScoreRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    tender_id: int
    total_score: int
    industry_score: int
    project_size_score: int
    location_score: int
    timeline_score: int
    reasons: str

class RequirementRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    requirement_type: str
    description: str
    required_value: str
    evidence: str
    decision: str
    confidence: float

class ReportRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    tender_id: int
    status: str
    readiness_score: int
    executive_summary: str
    risks: str
    missing_documents: str
    recommended_next_steps: str
    requirements: list[RequirementRead] = []
