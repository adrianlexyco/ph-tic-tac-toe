from typing import Optional
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class Player(Document):
    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = Field(default=None)

    class Settings:
        name = "users"
