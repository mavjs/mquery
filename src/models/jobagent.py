from sqlmodel import SQLModel, Field, Relationship
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.match import Job
    from ..models.agentgroup import AgentGroup


class JobAgent(SQLModel, table=True):
    """Information about job relating to a specific agent group."""

    id: Union[int, None] = Field(default=None, primary_key=True)
    task_in_progress: int

    job_id: int = Field(foreign_key="job.internal_id")
    job: "Job" = Relationship(back_populates="agents")

    agent_id: int = Field(foreign_key="agentgroup.id")
    agent: "AgentGroup" = Relationship(back_populates="jobs")
