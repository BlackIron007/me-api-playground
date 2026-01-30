# Me-API Playground (Backend Assessment - Track A)

## Live URLs

- **Backend API:** https://me-api-playground-ql1p.onrender.com
- **API Docs (Swagger):** https://me-api-playground-ql1p.onrender.com/docs
- **Frontend:** https://blackiron007.github.io/me-api-playground/

---

## Overview

This project is a minimal backend and frontend playground that stores my candidate profile in a database and exposes it via a REST API.
It demonstrates backend fundamentals such as API design, database modeling, query filtering, and frontend consumption.


---

## Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite (via SQLAlchemy ORM)
- **Frontend:** Plain HTML + JavaScript (Fetch API)
- **Hosting:** Render (Backend), Static HTML (Frontend)

---

## Architecture Overview

- The frontend consumes the backend via REST APIs.
- The backend handles validation, filtering, and database access.
- SQLite is used for simplicity and reproducibility.

---

## Database Schema

The database consists of two main tables:

### profile
Stores basic candidate information.

```sql
CREATE TABLE profile (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    education TEXT,
    github TEXT,
    linkedin TEXT,
    portfolio TEXT
);
```

### projects
Stores project details.

```sql
CREATE TABLE projects (
    id INTEGER PRIMARY KEY,
    title TEXT,
    description TEXT,
    skills TEXT,
    link TEXT
);
```

> Note:
Project skills are stored as a comma-separated string for simplicity. This is a conscious trade-off to reduce schema complexity within the assessment scope.

---

## API Endpoints

### Health Check

```bash
GET /health
```

> Returns 200 OK if the service is live.

### Profile

```bash
GET /profile
```

> Fetches or updates the candidate profile.

### Projects

```bash
GET /projects
GET /projects?skill=python
```

> Returns all projects or filters projects by skill.

### Search

```bash
GET /search?q=keyword
```

> Performs a simple substring search across project title, description, and skills.

### Top Skills

```bash
GET /skills/top
```

> Returns skills ranked by frequency across projects.

---

## Frontend
The frontend is a minimal HTML page that:
- Displays the candidate profile
- Lists projects
- Allows filtering projects by skill

It communicates with the backend using the Fetch API and demonstrates CORS-enabled API consumption.

---

## Local Setup

1. Clone the repository

```bash
git clone <repo-url>
cd me-api-playground
```


2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Seed the database

```bash
python -m app.seed
```

5. Run the backend

```bash
uvicorn app.main:app --reload
```
Open:
> API docs: http://127.0.0.1:8000/docs

> Frontend: Open frontend/index.html in browser

---

## Deployment

- Backend is deployed on Render.
- Frontend is a static HTML page that consumes the hosted API.
- Environment variables are used for configuration in production.
- The application automatically seeds initial data on startup if the database is empty. This ensures compatibility with free-tier hosting environments.

---

## Sample API Calls

```bash
curl /health
curl /projects?skill=python
curl /search?q=api
```

---

## Known Limitations & Trade-offs

- SQLite is used instead of PostgreSQL for faster setup and reproducibility.
- Skills are stored as comma-separated values rather than a normalized join table.
- No authentication is implemented for write operations.
- Search uses basic substring matching (no full-text search).
- Frontend is intentionally minimal and unstyled.
- These decisions were made to keep the scope small while maintaining a production-minded structure.

---

## Remarks

- If extended further, this project could include:
- Authentication for write operations
- Pagination for project listing
- Proper skill normalization
- Full-text search
- CI/CD and automated tests

---