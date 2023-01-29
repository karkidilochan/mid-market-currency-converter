from fastapi import APIRouter, HTTPException
from src.schemas.convert import ConvertResponse, ConvertMetadata
import httpx
from datetime import datetime
from src.utils.get_currencies import validate_currency
from src.db.session import db_context
from src.db.models.history import History
import logging

router = APIRouter()


@router.get("/",response_model=ConvertResponse, tags=["Converter"])
async def convert_currencies(amount: float, from_currency: str, to_currency: str):
    from_currency_is_valid = await validate_currency(from_currency)
    to_currency_is_valid = await validate_currency(to_currency)
    if (from_currency_is_valid and to_currency_is_valid):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"https://wise.com/rates/history+live?source={from_currency.lower()}&target={to_currency.lower()}&length=30&resolution=hourly&unit=day", headers= {
                    "content-type": "application/json"
                })
                exchange_rate = response.json()[-1]["value"]
                converted_amount = amount * exchange_rate
                time_of_conversion = datetime.now()
                result = ConvertResponse(converted_amount=converted_amount,rate=exchange_rate, metadata=ConvertMetadata(time_of_conversion=time_of_conversion, from_currency=from_currency, to_currency=to_currency))
                with db_context() as db:
                    db.add(History(**{"converted_amount":converted_amount,"rate": exchange_rate, "time_of_conversion": time_of_conversion, "from_currency": from_currency, "to_currency": to_currency}))
                    db.commit()
                return result
        except Exception as e:
            logging.exception(repr(e))
            raise HTTPException(
                status_code=500,
                detail=f"An error occurred while converting currency {repr(e)}",
            )
    else:
        raise HTTPException(status_code=400, detail="Please provide valid currency codes")
