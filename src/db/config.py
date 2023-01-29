# Database related config stored here.
# Stored separately from the global app related config in app/config.py because
# we also use this db/ code for the migrations service
import os

DB_HOST = os.getenv("POSTGRES_SERVER")
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
