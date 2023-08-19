from typing import Optional, Protocol
from uuid import UUID

from app.core.models.game import Game


class GameRepository(Protocol):
    async def create(self, player1_id: UUID, player2_id: UUID, board_size: str) -> Game:
        ...

    async def fetch_by_id(self, id: UUID) -> Optional[Game]:
        ...
