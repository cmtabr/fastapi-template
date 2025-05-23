# Migrations folder

## Overview
This folder contains the migration files for the database. Each migration file is responsible for a specific change to the database schema. The migration files are generated using the `alembic` tool, which is a lightweight database migration tool for use with SQLAlchemy.  

## Naming Convention
The migration files are named using the following convention:  
`<timestamp>_<migration_name>.py`  
Where `<timestamp>` is the timestamp when the migration was created, and `<migration_name>` is a short description of the migration.
For example:  
`2025-04-23_23:20:08_users_table_creation.py`
This naming convention helps to keep track of the order in which migrations were created and applied.

## Common Commands
- **Generate a new migration**:  
  To create a new migration file, run the following command:  
  ```bash
  alembic revision --autogenerate -m "migration_name"
  ```
  In the above command, remember to attend the naming convention.
  The `--autogenerate` flag will automatically generate the migration file based on the changes detected in the database schema.

  Or, if you want to create an empty migration file, run:  
  ```bash
    sh scripts/create_migration.sh
  ```
  This will create a new migration file in the `versions` directory with the current timestamp.

  Replace `migration_name` with a descriptive name for the migration.
- **Apply migrations**:
  To apply all pending migrations to the database, run the following command:  
  ```bash
  alembic upgrade head
  ```
- **Downgrade migrations**:
    To downgrade the database to a specific migration, run the following command:  
    ```bash
    alembic downgrade <revision>
    ```
    Replace `<revision>` with the revision ID of the migration you want to downgrade to.
- **Show current revision**:
    To show the current revision of the database, run the following command:  
    ```bash
    alembic current
    ```
- **Show migration history**:
    To show the history of migrations, run the following command:  
    ```bash
    alembic history
    ```
- **Show migration details**:
    To show the details of a specific migration, run the following command:  
    ```bash
    alembic show <revision>
    ```
    Replace `<revision>` with the revision ID of the migration you want to view.
