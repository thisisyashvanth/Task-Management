

from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.routes.putTasks import todo_router
from api.routes.deleteTasks import task_router
from api.routes import deleteTasks
from api.routes.taskRouter import taskRouter
from core.database import Base, engine

Base.metadata.create_all(bind=engine)
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine, lifespan=lifespan)
    yield
app.include_router(todo_router)


app = FastAPI(title="Task App", lifespan=lifespan)

app.include_router(task_router)
app.include_router(taskRouter)
app.include_router(tasks.router)

