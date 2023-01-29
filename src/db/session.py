from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.db import config

engine = create_engine(config.DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def db_context() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
        db.commit()
        db.close()
    except Exception as e:
        db.rollback()
        db.close()
        raise e  # So that error can be handled downstream
