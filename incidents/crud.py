"""
CRUD operations:
"""

from app.core.models import (
    Incident,
    IncidentStatus,
    Component,
    ComponentAttribute,
)

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from .schemas import IncidentCreate


async def get_component_by_name_and_attributes(
    session: AsyncSession, name: str, attributes: list[dict[str, str]]
) -> list[Component]:
    query = (
        select(Component)
        .filter(Component.name == name)
        .join(Component.attributes)
        .filter(
            ComponentAttribute.name.in_([attr["name"] for attr in attributes]),
            ComponentAttribute.value.in_(
                [attr["value"] for attr in attributes]
            ),
        )
    )

    result = await session.execute(query)
    return list(result.scalars().all())


async def get_incidents(session: AsyncSession) -> list[Incident]:
    query = (
        select(Incident)
        .options(selectinload(Incident.updates))
        .order_by(Incident.id)
    )
    result: Result = await session.execute(query)
    incidents = result.scalars().all()
    return list(incidents)


async def get_incident(
    session: AsyncSession, incident_id: int
) -> Incident | None:
    return await session.get(
        Incident, incident_id, options=[selectinload(Incident.updates)]
    )


async def create_incident(
    session: AsyncSession, incident_in: IncidentCreate
) -> Incident | None:
    updates = [
        IncidentStatus(status=upd.status, text=upd.text)
        for upd in incident_in.updates
    ]
    components = []

    for comp_data in incident_in.components:
        comp_instance = await get_component_by_name_and_attributes(
            session=session,
            name=comp_data.name,
            attributes=[
                {"name": attr.name, "value": attr.value}
                for attr in comp_data.attributes
            ],
        )

        if not comp_instance:
            return None

        components.extend(comp_instance)

    incident = Incident(
        text=incident_in.text,
        impact=incident_in.impact,
        start_date=incident_in.start_date,
        end_date=incident_in.end_date,
        components=components,
        updates=updates,
    )

    session.add(incident)
    await session.commit()
    await session.refresh(incident)
    return incident
