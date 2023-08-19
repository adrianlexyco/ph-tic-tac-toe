from typing import Protocol
from uuid import UUID

from app.core.models.player import Player



class PlayerRepository(Protocol):
    async def create(self, name: str) -> Player:
        ...

    async def fetch_by_id(self, id: UUID) -> Player:
        ...
