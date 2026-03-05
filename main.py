
from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine
from api.routes.putTasks import todo_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine, lifespan=lifespan)
    yield

app = FastAPI(title="Task App")
app.include_router(todo_router)
