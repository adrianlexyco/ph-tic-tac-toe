from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Player(BaseModel):
    id: Optional[UUID]
    name: Optional[str]

    class Config:
        orm_mode = True