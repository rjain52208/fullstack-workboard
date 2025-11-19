from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


TaskStatus = Literal["todo", "in_progress", "done"]


class TaskBase(BaseModel):
    title: str
    status: TaskStatus = "todo"
    description: Optional[str] = None


class TaskOut(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
