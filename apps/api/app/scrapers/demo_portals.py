from datetime import datetime, timedelta, timezone
from app.scrapers.base import ScrapedTender, TenderScraper

class GeMDemoScraper(TenderScraper):
    async def scrape(self) -> list[ScrapedTender]:
        now = datetime.now(timezone.utc)
        return [ScrapedTender("GeM", "GEM-2026-AI-001", "AI-enabled procurement analytics dashboard", "Ministry of Commerce", "software", "Delhi", 4_200_000, now, now + timedelta(days=21), "https://gem.gov.in/", {"mode": "demo"})]

class CPPPDemoScraper(TenderScraper):
    async def scrape(self) -> list[ScrapedTender]:
        now = datetime.now(timezone.utc)
        return [ScrapedTender("CPPP", "CPPP-2026-CLOUD-018", "Cloud based document workflow automation system", "Central Public Works Department", "cloud software", "India", 8_500_000, now, now + timedelta(days=34), "https://eprocure.gov.in/", {"mode": "demo"})]
