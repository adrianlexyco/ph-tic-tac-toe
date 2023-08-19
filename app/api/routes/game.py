from fastapi import APIRouter

router = APIRouter(tags=["games"], prefix="/games")


@router.get("/games/")
async def read_games():
    return
