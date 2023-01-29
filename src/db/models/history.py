from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Float, DateTime, Integer
from .base import Base


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, autoincrement=True)
    converted_amount = Column(Float)
    rate = Column(Float)
    time_of_conversion = Column(DateTime)
    from_currency = Column(String)
    to_currency = Column(String)
