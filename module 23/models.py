from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    derector: str

class Movie(MovieCreate):
    id:int