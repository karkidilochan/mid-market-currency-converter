from fastapi import APIRouter
from src.utils.get_currencies import scrape_currencies

router = APIRouter()

@router.get("/",response_model=dict, tags=["Currencies"])
async def list_all_currencies():
    result = await scrape_currencies()
    return result
