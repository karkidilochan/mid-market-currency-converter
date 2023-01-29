import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException
from src.service.redis import redis_client
import logging

async def scrape_currencies():
    try:
        request_url = "https://wise.com/gb/currency-converter/currencies"
        cached_response = redis_client.get(request_url)
        if not cached_response:
            async with httpx.AsyncClient() as client:
                response = await client.get(request_url)
                redis_client.set(request_url, response.text)
                cached_response = response.text
        soup = BeautifulSoup(cached_response, "html.parser")
        result = {}
        currency_cards = soup.find_all("a", {"aria-label": "currency-card"})
        for card in currency_cards:
            result[str(card.find("p", class_="currencies_currencyCard__currencyName__wj5_u").text)] = card.find("h5", class_= "currencies_currencyCard__currencyCode__RG8bp").text
        return result
    except Exception as e:
        logging.exception(repr(e))
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while fetching currencies {repr(e)}",
        )

async def validate_currency(currency_code: str):
    currencies = await scrape_currencies()
    return currency_code in currencies.values()
