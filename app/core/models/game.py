from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID

class GameMovements(BaseModel):
    board_position: str

class Game(BaseModel):
    id: Optional[UUID]
    player1_id: Optional[UUID]
    player2_id: Optional[UUID]
    board_size: Optional[int]
    movements: Optional[List[GameMovements]]

    class Config:
        orm_mode = True