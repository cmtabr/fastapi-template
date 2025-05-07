#!/bin/sh

GREEN="\e[92m"
PURPLE="\e[35m"
ORANGE="\e[38;5;208m"
RESET="\e[0m"
WHITE="\e[97m"

API_ENV_FILE="api/.env"
DOT_ENV_FILE=".env"

secret_generator() {
    python3 -c 'import secrets; print(secrets.token_urlsafe(64))'
}

loading_spinner() {
    local pid=$!
    local delay=0.1
    local spinstr='|/-\'
    tput civis
    while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
        local temp=${spinstr#?}
        printf " ${PURPLE}[%c]${RESET}  " "$spinstr"
        local spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\b\b\b\b\b\b"
    done
    printf "    \b\b\b\b"
    tput cnorm
}

add_var() {
    local var=$1
    local value=$2
    shift 2
    local targets=("$@")

    printf "${PURPLE}Adding %s ${RESET}" "$var"
    (sleep 0.7) &
    loading_spinner

    printf "\r${PURPLE}Adding %s${RESET}\n" "$var"

    for target in "${targets[@]}"; do
        echo "${var}=${value}" >> "$target"
    done
}

printf "${ORANGE}Generating environment files${RESET}\n"
printf "${WHITE}----------------------------${RESET}\n"

echo "# API enviroment variables" > "$API_ENV_FILE"
echo "# Public environment variables" > "$DOT_ENV_FILE"

add_var "AUTH_SECRET" "$(secret_generator)" "$API_ENV_FILE"
add_var "AUTH_ALGORITHM" "HS256" "$API_ENV_FILE"

echo -e "\n# Postgres enviroment variables" >> api/.env

add_var "POSTGRES_USER" "postgres" "$API_ENV_FILE" "$DOT_ENV_FILE"
add_var "POSTGRES_PASSWORD" "password" "$API_ENV_FILE" "$DOT_ENV_FILE"
add_var "POSTGRES_HOST" "postgres" "$API_ENV_FILE" # docker-compose service name
add_var "POSTGRES_PORT" "5432" "$API_ENV_FILE" "$DOT_ENV_FILE"
add_var "POSTGRES_DATABASE" "database" "$API_ENV_FILE" "$DOT_ENV_FILE"

printf "\n${GREEN}Enviroment Setup | Enviroment variables added to '${API_ENV_FILE}' and '${DOT_ENV_FILE}' successfully${RESET}\n"
