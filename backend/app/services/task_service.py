from datetime import datetime
from typing import List

from app.schemas.task import TaskOut


# In a real project this would be backed by PostgreSQL.
# Here we simulate a tiny in-memory "database".
_FAKE_DB = [
    TaskOut(
        id=1,
        title="Set up project structure",
        status="todo",
        description="Create backend/frontend folders and basic config.",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    ),
    TaskOut(
        id=2,
        title="Wire FastAPI + React",
        status="in_progress",
        description="Expose /tasks API and consume from frontend.",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    ),
    TaskOut(
        id=3,
        title="Write unit tests",
        status="done",
        description="Add pytest tests for health + tasks endpoints.",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    ),
]


def list_tasks() -> List[TaskOut]:
    """Return all tasks from the fake in-memory store."""
    return _FAKE_DB
