# FastAPI Project Template
This repository purpose is to present a simple API using FastAPI webframework. Here i handle with the framework on subject to serve as an API, but it does contans some basic CRUD operations and authentication using JWT tokens. The project is structured to be easily extendable and maintainable.

# How to run the project
1. Clone the repository:
   1. Using HTTPS:
   ```bash
   git clone https://github.com/cmtabr/fastapi-template.git
    ```
   2. Using SSH:
   ```bash
   git clone git@github.com:cmtabr/fastapi-template.git
   ```
   3. Using GitHub CLI:
   ```bash
   gh repo clone cmtabr/fastapi-template
   ```
2. Navigate to the project directory:
   ```bash
   cd fastapi-template/src
   ```
3. create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
    1. On Windows:
      ```bash
      venv\Scripts\activate
      ```
    2. On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```
5. Install the dependencies:
    ```bash
    pip install -r api/requirements.txt
    pip install alembic
    ```
6. Create environment variables:
   ```bash
    bash scripts/enviroment_setup.sh
    ```
   This script will create a `.env` file with the necessary environment variables for the project.

7. Build and run the Docker container:
   ```bash
   docker-compose up --build
   ```
8. Run the Alembic migrations:
   ```bash
    alembic upgrade head
    ```
9. Access the API documentation:
    1. Open your web browser and go to `http://localhost:5000/docs` for Swagger UI

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
│   └── enviroment_setup.sh
├── .gitignore
├── alembic.ini
└── docker-compose.yml
```
