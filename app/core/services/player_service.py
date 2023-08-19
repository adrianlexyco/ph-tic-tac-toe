from app.core.models.player import Player
from app.core.protocols.player_repository import PlayerRepository


async def create(player_repository: PlayerRepository, name: str) -> Player:
    player = await player_repository.create(name=name)

    return player
