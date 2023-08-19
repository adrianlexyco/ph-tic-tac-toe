from typing import Optional, Protocol
from uuid import UUID

from app.core.models.player import Player

from ..models.player import Player as PlayerModel


async def create(name) -> Player:
    player = await PlayerModel(name=name).create()

    return player


async def fetch_by_id(id: UUID) -> Optional[Player]:
    player = await PlayerModel.find_one(PlayerModel.id == id)

    if not player:
        return None

    return player
