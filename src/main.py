import os
from fastapi import FastAPI
from src.config import settings
from src.api.api import router
from fastapi.middleware.cors import CORSMiddleware
from src.db.utils import run_migrations

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url=f"{settings.API_STR}/docs",
    openapi_url=f"{settings.API_STR}/openapi.json",
)


@app.on_event("startup")
async def startup():
    run_migrations()


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS_LIST,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router, prefix=settings.API_STR)
