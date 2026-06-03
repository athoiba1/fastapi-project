# FastAPI Project

A production-ready REST API built with FastAPI, featuring authentication, database integration, and comprehensive testing.

## Features

- **FastAPI** - Modern, fast web framework with auto-generated docs
- **Authentication** - JWT-based auth with bcrypt password hashing
- **Database** - SQLAlchemy ORM with async support
- **Validation** - Pydantic schemas for request/response validation
- **Testing** - Pytest with async test support
- **Docker** - Ready for containerized deployment

## Project Structure

```
fastapi-project/
├── app/
│   ├── core/           # Config, security, dependencies
│   ├── models/         # SQLAlchemy database models
│   ├── routers/        # API route handlers
│   ├── schemas/        # Pydantic request/response models
│   ├── services/       # Business logic layer
│   └── main.py         # Application entry point
├── tests/              # Test suite
├── docs/               # API documentation
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/fastapi-project.git
cd fastapi-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
# Edit .env with your settings
```

## Run

```bash
# Development
uvicorn app.main:app --reload

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/docs for interactive API documentation.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `POST` | `/auth/register` | Register new user |
| `POST` | `/auth/login` | Login and get token |
| `GET` | `/users/me` | Get current user |
| `GET` | `/items` | List items |
| `POST` | `/items` | Create item |
| `GET` | `/items/{id}` | Get item by ID |
| `PUT` | `/items/{id}` | Update item |
| `DELETE` | `/items/{id}` | Delete item |

## Docker

```bash
docker-compose up --build
```

## License

MIT
