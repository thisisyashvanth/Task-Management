



from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from core.deps import get_db
from models.Tasks import Tasks
from schemas.schemas import TaskResponse


taskRouter = APIRouter(prefix="/task", tags=["Task Routes"])

@taskRouter.get("/", response_model=list[TaskResponse])
def get_all_todos(db: Session = Depends(get_db)):
    tasks = db.execute(select(Tasks)).scalars().all()
    return tasks
    
