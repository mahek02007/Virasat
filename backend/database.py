"""
Virasat — Database Engine & Session
Local dev: SQLite  |  Production: Supabase/PostgreSQL (swap DATABASE_URL in .env)
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Falls back to local SQLite if DATABASE_URL is not set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./virasat.db")

# SQLite needs check_same_thread=False; PostgreSQL ignores this kwarg via connect_args
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Modern SQLAlchemy 2.0 Base class."""
    pass


def get_db():
    """FastAPI dependency: yields a SQLAlchemy session, closes on completion."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
