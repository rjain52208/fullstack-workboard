from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.services.task_service import list_tasks


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Backend API for a simple task management dashboard.",
)

# In a real project, allowed origins would come from configuration
origins = ["http://localhost:3000", "http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["health"])
def health_check():
    """
    Simple health-check endpoint so the frontend / DevOps can verify the API is alive.
    """
    return {
        "status": "ok",
        "service": "fullstack-workboard-backend",
        "environment": settings.environment,
    }


@app.get("/tasks", tags=["tasks"])
def get_tasks():
    """
    Return a list of tasks from the (simulated) data store.

    In a real project this would query PostgreSQL via SQLAlchemy.
    """
    tasks = list_tasks()
    return {"tasks": tasks}
