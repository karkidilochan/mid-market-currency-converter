from fastapi import APIRouter, HTTPException
from src.schemas.convert import ConvertResponse, ConvertMetadata
from src.db.session import db_context
from src.db.models.history import History
import logging

router = APIRouter()


@router.get("/",response_model=list[ConvertResponse], tags=["History"])
async def get_history():
    try:
        with db_context() as db:
            result = (
                db.query(History)
                .order_by(History.time_of_conversion.desc())
                .all()
            )
            response = list(map(lambda x: ConvertResponse(converted_amount=x.converted_amount,rate=x.rate, metadata=ConvertMetadata(time_of_conversion=x.time_of_conversion, from_currency=x.from_currency, to_currency=x.to_currency)), result))
            return response

    except Exception as e:
        logging.exception(repr(e))
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while converting currency {repr(e)}",
        )
