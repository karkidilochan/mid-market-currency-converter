from typing import Any, Dict, List, Optional
from pydantic import BaseSettings
from pydantic.class_validators import validator


class Settings(BaseSettings):
    API_STR: str = "/api"
    APP_ENV: str = "development"
    PROJECT_NAME: str = "Mid-market Currency Converter"

    CORS_ORIGINS: str
    CORS_ORIGINS_LIST: Optional[List[str]] = None

    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    API_KEY_NAME: str
    API_KEY: str

    # This will build the CORS_ORIGINS list
    @validator("CORS_ORIGINS_LIST", pre=True)
    def build_cors_origins(
        cls, v: Optional[List], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, List):
            return v
        cors_origins = values.get("CORS_ORIGINS")
        if not cors_origins:
            return []
        else:
            cors_list = [origin.strip() for origin in cors_origins.split(",")]
            return cors_list

    class Config:
        case_sensitive = True


settings = Settings()
