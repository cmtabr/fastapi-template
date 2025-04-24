#!/bin/bash

secret_generator() {
    python3 -c 'import secrets; print(secrets.token_urlsafe(64))'
}

(
    echo '# API dependency variables'
    echo AUTH_SECRET=$(secret_generator)
    echo AUTH_ALGORITHM=HS256
    echo
    echo '# Postgres stuff'
    echo POSTGRES_USER=postgres
    echo POSTGRES_PASSWORD=password
    echo POSTGRES_HOST=postgres # docker-compose service name
    echo POSTGRES_PORT=5432
    echo POSTGRES_DATABASE=database
) > api/.env

echo "API | Example enviroment file and variables created successfully"
echo

(
    echo '# Postgres dependency variables'
    echo POSTGRES_USER=postgres
    echo POSTGRES_PASSWORD=password
    echo POSTGRES_DATABASE=database
) > .env

echo "DATABASE | Example enviroment file and variables created successfully"
