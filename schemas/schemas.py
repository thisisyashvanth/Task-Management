from pydantic import BaseModel


class deleteResponse(BaseModel):
    msg:str

class deleteRequest(BaseModel):
    id:int
    