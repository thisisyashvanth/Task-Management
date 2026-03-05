from fastapi import FastAPI
from core.database import Base, engine
from api.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(tasks.router)