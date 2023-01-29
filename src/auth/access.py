from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

from src.config import settings

api_key_header = APIKeyHeader(name=settings.API_KEY_NAME, auto_error=False)


async def get_api_key_authorized(
    api_key_header: str = Security(api_key_header),
):

    if (api_key_header == settings.API_KEY):
        return settings.API_KEY
    else:
        raise HTTPException(
            detail=dict(message="Unauthorized access. Couldn't verify access token."),
            status_code=status.HTTP_403_FORBIDDEN,
            headers={
                "WWW-Authenticate": "Bearer",
            },
        )
