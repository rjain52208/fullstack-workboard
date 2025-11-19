from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Fullstack Workboard API",
    version="0.1.0",
    description="Backend API for a simple task management dashboard.",
)

# In a real project, allowed origins would be environment-driven
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
    Simple health-check endpoint so the frontend / devops can verify the API is alive.
    """
    return {"status": "ok", "service": "fullstack-workboard-backend"}


# Placeholder in-memory "tasks" so the API looks realistic
FAKE_TASKS = [
    {"id": 1, "title": "Set up project structure", "status": "todo"},
    {"id": 2, "title": "Wire FastAPI + React", "status": "in_progress"},
    {"id": 3, "title": "Write unit tests", "status": "done"},
]


@app.get("/tasks", tags=["tasks"])
def list_tasks():
    """
    Return a simple list of tasks. In a real project this would hit PostgreSQL via SQLAlchemy.
    """
    return {"tasks": FAKE_TASKS}
