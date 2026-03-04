from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import engine

from core.database import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task App")