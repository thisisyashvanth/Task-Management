from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from core.deps import get_db
from models.Tasks import Todo
from schemas.schemas import deleteResponse


 
task_router = APIRouter(prefix="/delete", tags=["task"])
 

 
@task_router.delete("/{id}", response_model=deleteResponse)
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.get(Todo, id)
    if not task:
        raise HTTPException(status_code=404, detail=(f"Deleted Successfully"))
    db.delete(db.get(Todo, id))
    db.commit()
    return "Success"