from fastapi import FastAPI
from api.routes.taskRouter import taskRouter
from core.database import Base
from core.database import Base, engine
from api.routes import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app = FastAPI(title="Task App", lifespan=lifespan)

app.include_router(taskRouter)
app.include_router(tasks.router)
