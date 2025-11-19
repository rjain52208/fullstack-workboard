# Fullstack Workboard – Task Management Dashboard

A full-stack **task manager / workboard** built with a FastAPI backend and a React frontend. This project simulates a real engineering codebase with backend + frontend separation, tests, PostgreSQL integration, and Docker-based environment setup.

---

## 📁 Project Structure

```
fullstack-workboard/
  backend/
    app/
      api/          # FastAPI routes (auth, tasks)
      models/       # SQLAlchemy models
      schemas/      # Pydantic request/response schemas
      services/     # Business logic layer
      core/         # config, db session, security
    tests/
      test_auth.py
      test_tasks.py
    pyproject.toml / requirements.txt
    Dockerfile

  frontend/
    src/
      components/   # Reusable UI components
      pages/        # Login, Dashboard, Workboard
      api/          # API client to talk to FastAPI backend
      hooks/        # useAuth, useTasks, useBoardState
    src/tests/
    package.json
    Dockerfile

  docker-compose.yml
  README.md
```

---

## ⚙️ Backend (FastAPI)

The backend provides a simple REST API for user authentication and task management. It follows clean architecture guidelines:

- `api/` → route handlers (`/auth/login`, `/tasks`, `/tasks/{id}`)
- `models/` → SQLAlchemy ORM models (`User`, `Task`)
- `schemas/` → Pydantic schemas for validation
- `services/` → business logic (create tasks, update status, verify login)
- `core/` → centralized config, DB connection, security utils

Tests in `tests/` use FastAPI's TestClient to mock login and CRUD task scenarios.

---

## 🎨 Frontend (React)

The React frontend renders a lightweight SPA:

- **Login Page** → mock auth workflow
- **Dashboard** → counts of completed / pending tasks
- **Workboard** → basic 3-column Kanban (Todo / In-Progress / Done)

Folder structure:

- `components/` → TaskCard, Column, Layout
- `pages/` → Login, Dashboard, Board
- `api/` → JS fetch wrappers for backend routes
- `hooks/` → `useTasks`, `useAuth`, local state management

---

## 🐳 Docker Setup (Conceptual)

> You do **not** need to run anything — this layout simply makes the repo look production-ready.

### backend/Dockerfile  
- Python image with FastAPI + Uvicorn  
- Installs backend `requirements.txt`  
- Exposes port 8000

### frontend/Dockerfile  
- Node image  
- Installs dependencies from `package.json`  
- Runs React dev or production server

### docker-compose.yml  
- `db` → PostgreSQL  
- `backend` → FastAPI service  
- `frontend` → React UI  
- Services share networks & environment variables

---

## ✅ What This Project Demonstrates

This structure highlights:

- Full-stack engineering (API + UI + DB)
- Separation of concerns in backend and frontend
- Realistic production layout with Docker & PostgreSQL
- Awareness of testing patterns
- Ability to structure maintainable software like real SWE teams
