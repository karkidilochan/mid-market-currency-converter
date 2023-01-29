from fastapi import APIRouter, Depends
from src.config import settings
from src.api.currencies import router as currencies_router
from src.api.convert import router as convert_router
from src.api.history import router as history_router
from src.auth.access import get_api_key_authorized

router = APIRouter()


@router.get("/", tags=["General"])
async def show_info():
    return {
        "mode": settings.APP_ENV,
        "message": f"Mid-market Currency Converter. {settings.APP_ENV} mode",
    }

router.include_router(router=currencies_router, prefix="/currencies",dependencies=[Depends(get_api_key_authorized)])
router.include_router(router=convert_router, prefix="/convert",dependencies=[Depends(get_api_key_authorized)])
router.include_router(router=history_router, prefix="/history",dependencies=[Depends(get_api_key_authorized)])
