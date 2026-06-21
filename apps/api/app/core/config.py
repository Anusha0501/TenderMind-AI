from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "TenderMind-AI"
    environment: str = Field(default="development")
    database_url: str = Field(default="sqlite:///./tendermind.db")
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])
    gemini_api_key: str | None = None
    langsmith_api_key: str | None = None
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
