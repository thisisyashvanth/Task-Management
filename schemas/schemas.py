from pydantic import BaseModel

class TodoRequest(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    class Config:
        from_attributes = True