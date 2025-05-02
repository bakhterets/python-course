from datetime import datetime
from typing import List
from typing import Optional

from app.api_v1.components.schemas import ComponentBase
from app.datetime import datetime_utcnow

from pydantic import BaseModel
from pydantic import ConfigDict


class IncidentStatusBase(BaseModel):
    status: str
    text: str
    timestamp: datetime = datetime_utcnow()
    model_config = ConfigDict(from_attributes=True)


class IncidentBase(BaseModel):
    id: int
    text: str
    impact: int
    start_date: datetime
    end_date: Optional[datetime] = None
    updates: List[IncidentStatusBase] = []
    model_config = ConfigDict(from_attributes=True)


class IncidentCreate(IncidentBase):
    components: List[ComponentBase]


class IncidentUpdate(IncidentCreate):
    pass


class IncidentRead(IncidentBase):
    components: List[ComponentBase]
