# FastAPI Project Template
This repository purpose is to present a simple API using FastAPI webframework. Here i handle with the framework on subject to serve as an API, but it does contans some basic CRUD operations and authentication using JWT tokens. The project is structured to be easily extendable and maintainable.

# Project Structure
```bash
src/
├── api/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── auth_settings.py
│   │   └── database_settings.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── shared.py
│   │   └── users.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth_router.py
│   │   └── user_router.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── token_schema.py
│   │   └── user_schema.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── session_manager.py
│   │   └── token_handler.py
│   ├── .dockerignore
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── migrations/
│   ├── versions/
│   │   └── ...
│   ├── env.py
│   ├── README.md
│   ├── script.py.mako
├── scripts/
│   ├── create_migration.sh
│   └── setup.sh
├── .dockerignore
├── .gitignore
├── alembic.ini
└── docker-compose.yml
```
