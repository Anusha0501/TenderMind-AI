from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from app.db import get_session
from app.models.domain import ExtractedRequirement
from app.schemas.tenders import ReportRead, ScoreRead, TenderRead
from app.services.tenders import TenderService

router = APIRouter(prefix="/api/v1", tags=["tenders"])

@router.post("/jobs/scrape", response_model=list[TenderRead])
async def scrape_sources(session: Session = Depends(get_session)):
    return await TenderService(session).scrape_demo_sources()

@router.get("/tenders", response_model=list[TenderRead])
def list_tenders(session: Session = Depends(get_session)):
    return TenderService(session).list_tenders()

@router.post("/tenders/{tender_id}/score", response_model=ScoreRead)
def score_tender(tender_id: int, session: Session = Depends(get_session)):
    try:
        return TenderService(session).score_tender(tender_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

@router.post("/tenders/{tender_id}/analyze", response_model=ReportRead)
def analyze_tender(tender_id: int, session: Session = Depends(get_session)):
    try:
        report, requirements = TenderService(session).analyze_tender(tender_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    data = ReportRead.model_validate(report)
    data.requirements = requirements
    return data
