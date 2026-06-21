from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ScrapedTender:
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
    raw_payload: dict[str, object]

class TenderScraper(ABC):
    @abstractmethod
    async def scrape(self) -> list[ScrapedTender]:
        """Return normalized tenders from a portal adapter."""
