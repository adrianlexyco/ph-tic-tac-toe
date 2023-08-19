from typing import Optional
import uuid
from app.core.models.player import Player
from app.core.protocols.player_repository import PlayerRepository
from app.core.services.exceptions import GenericError


async def create(player_repository: PlayerRepository, name: str) -> Player:
    player = await player_repository.create(name=name)

    return player

async def fetch_by_id(player_repository: PlayerRepository, id: uuid) -> Optional[Player]:
    player = await player_repository.fetch_by_id(id=id)

    if not player:
        raise GenericError(error="user.not.found")

    return player
