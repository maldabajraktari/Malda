from pydantic import BaseModel
from typing import OPtional

class Item(BaseModel):
    id: Optional[int]=None
    name: str
    description: Optional[str]=None