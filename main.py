from contextlib import asynccontextmanager
from api.routes.deleteTasks import task_router
from fastapi import FastAPI
from sqlalchemy import engine

from api.routes import deleteTasks
from core.database import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task App")
app.include_router(task_router)