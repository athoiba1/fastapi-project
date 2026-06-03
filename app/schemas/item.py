from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ItemCreate(BaseModel):
    title: str
    description: str = ""
    price: float


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None


class ItemResponse(BaseModel):
    id: int
    title: str
    description: str
    price: float
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
