"""
Virasat — Database Engine & Session
Local dev: SQLite  |  Production: Supabase/PostgreSQL (set DATABASE_URL in .env)

Supabase connection notes:
  - Use the Transaction Pooler URL (port 6543) from your Supabase dashboard.
  - Prefix the URL with postgresql+psycopg2:// (not plain postgresql://).
  - pool_pre_ping=True handles dropped idle connections behind Supabase's pooler.
  - NullPool is used for serverless/thread-per-request patterns (avoids stale connections).
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv

load_dotenv()

# Falls back to local SQLite if DATABASE_URL is not set
_raw_url = os.getenv("DATABASE_URL", "sqlite:///./virasat.db")

# Normalise: some tools emit "postgres://" but SQLAlchemy 2.x requires "postgresql+psycopg2://"
if _raw_url.startswith("postgres://"):
    _raw_url = _raw_url.replace("postgres://", "postgresql+psycopg2://", 1)
elif _raw_url.startswith("postgresql://") and "+psycopg2" not in _raw_url:
    _raw_url = _raw_url.replace("postgresql://", "postgresql+psycopg2://", 1)

DATABASE_URL = _raw_url
IS_SQLITE = DATABASE_URL.startswith("sqlite")

if IS_SQLITE:
    # SQLite needs check_same_thread=False for FastAPI's thread-per-request model
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=False,
    )
else:
    # PostgreSQL / Supabase
    # NullPool: each request gets a fresh connection returned to Supabase's own pooler
    # pool_pre_ping: validates the connection before use (handles pooler idle timeouts)
    engine = create_engine(
        DATABASE_URL,
        poolclass=NullPool,
        pool_pre_ping=True,
        echo=False,
    )

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
