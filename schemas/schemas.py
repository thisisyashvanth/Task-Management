from pydantic import BaseModel

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config:
        from_attributes = True
