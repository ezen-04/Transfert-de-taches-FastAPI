from pydantic import BaseModel
from typing import Any


class AjouteResponse(BaseModel):
    id: int
    data: Any

    class Config:
        from_attributes = True
