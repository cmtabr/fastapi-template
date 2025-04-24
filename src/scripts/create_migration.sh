#!/bin/bash

VERSIONS_DIR="migrations/versions"

read -p "Enter revision message (e.g., users_table_creation): " MSG

MSG_SLUG=$(echo "$MSG" | tr ' ' '_' | tr -cd '[:alnum:]_')

alembic revision -m "$MSG_SLUG"

sleep 1

FILE=$(ls -t "$VERSIONS_DIR"/*_"$MSG_SLUG".py | head -n 1)

TIMESTAMP=$(date "+%Y-%m-%d_%H:%M:%S")

NEW_FILE="$VERSIONS_DIR/${TIMESTAMP}_${MSG_SLUG}.py"

mv "$FILE" "$NEW_FILE"

echo "Revision file renamed to:"
echo "$NEW_FILE"
