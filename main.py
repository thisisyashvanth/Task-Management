from contextlib import asynccontextmanager

from fastapi import FastAPI
from core.database import engine
from api.routes.taskRouter import taskRouter
from core.database import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="Task App", lifespan=lifespan)

app.include_router(taskRouter)