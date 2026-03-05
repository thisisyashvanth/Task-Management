from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from models.Tasks import Tasks
from schemas.schemas import TodoRequest, TodoResponse
from core.deps import get_db
from sqlalchemy.orm import Session
 
todo_router = APIRouter(prefix="/todo", tags=["Todo Routes"])

@todo_router.put("/{id}", response_model=TodoResponse)
def update_todo(id: int, todo: TodoRequest, db: Session = Depends(get_db)):
    
    existing_todo = db.get(Tasks, id)

    if not existing_todo:
        raise HTTPException(status_code=404, detail=f"Todo with id: {id} not found")

    existing_todo.title = todo.title
    existing_todo.description = todo.description
    existing_todo.is_completed = todo.is_completed

    db.commit()
    db.refresh(existing_todo)

    return existing_todo