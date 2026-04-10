from pydantic import BaseModel
from typing import Any, Optional


class RecuCreate(BaseModel):
    source: str
    payload: dict


class RecuResponse(BaseModel):
    id: int
    payload: Any
    response: Optional[Any]

    class Config:
        from_attributes = True
