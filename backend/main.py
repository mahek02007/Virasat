"""
Virasat — FastAPI Application Entry Point
Stack: FastAPI → SQLite (local dev) → Supabase/PostgreSQL (production)
Architecture: Region, ContentItem, Place, Media, Source
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from database import engine, Base
from routers import regions, content, places, facts, chat, search


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create all tables on startup (no Alembic needed for local dev)."""
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Virasat API",
    description=(
        "Backend for Virasat — The Heritage of India.\n\n"
        "Serves structured regional cultural data (Regions, ContentItems, Places, Media, Sources), "
        "cultural facts, unified search, and AI chat."
    ),
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)

# ── CORS ─────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers (v1) ─────────────────────────────────────────────────────────────
app.include_router(regions.router)
app.include_router(content.router)
app.include_router(places.router)
app.include_router(facts.router)
app.include_router(chat.router)
app.include_router(search.router)


# ── Health / Root ─────────────────────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {
        "status": "ok",
        "service": "Virasat API",
        "version": "1.0.0",
        "endpoints": {
            "regions": "/api/v1/regions",
            "content": "/api/v1/content",
            "places": "/api/v1/places",
            "facts": "/api/v1/facts",
            "search": "/api/v1/search",
            "chat": "/api/v1/chat",
            "docs": "/docs"
        }
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "healthy"}
