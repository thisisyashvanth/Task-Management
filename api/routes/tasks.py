from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.deps import get_db
from models.Tasks import Task

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
def create_task(title: str, description: str, db: Session = Depends(get_db)):

    new_task = Task(
        title=title,
        description=description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
    "message": "Task created successfully",
    "task": {
        "id": new_task.id,
        "title": new_task.title,
        "description": new_task.description,
        "is_completed": new_task.is_completed
    }
}