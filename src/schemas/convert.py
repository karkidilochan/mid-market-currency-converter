from pydantic import BaseModel
from datetime import datetime

class ConvertMetadata(BaseModel):
    time_of_conversion: datetime
    from_currency: str
    to_currency: str

class ConvertResponse(BaseModel):
    converted_amount: float
    rate: float
    metadata: ConvertMetadata
