from contextlib import asynccontextmanager
from api.routes.deleteTasks import task_router
from fastapi import FastAPI
from sqlalchemy import engine

from api.routes import deleteTasks
from api.routes.taskRouter import taskRouter
from core.database import Base, engine
from api.routes import tasks

Base.metadata.create_all(bind=engine)


app = FastAPI(title="Task App", lifespan=lifespan)

app.include_router(task_router)
app.include_router(taskRouter)
app.include_router(tasks.router)
