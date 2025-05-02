from app.core.models.db_manager import db_manager

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import IncidentCreate
from .schemas import IncidentRead

router = APIRouter(tags=["Incidents"])


@router.get("/", response_model=list[IncidentRead])
async def get_incidents(
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    return await crud.get_incidents(session=session)


@router.get("/{incident_id}", response_model=IncidentRead)
async def get_incident(
    incident_id: int,
    session: AsyncSession = Depends(db_manager.session_dependency),
):
    incident = await crud.get_incident(
        session=session,
        incident_id=incident_id,
    )
    if incident is not None:
        return incident

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Incident with id: {incident_id} not found",
    )


@router.post("/", response_model=IncidentRead)
async def create_component(
    incident_in: IncidentCreate,
    session: AsyncSession = Depends(db_manager.session_dependency),
):

    incident = await crud.create_incident(
        session=session, incident_in=incident_in
    )

    if not incident:
        raise HTTPException(
            status_code=404, detail="One or more components were not found."
        )

    return incident
