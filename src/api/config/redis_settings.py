from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    """
    RedisSettings handles configuration settings for the environment.

    This class inherits from BaseSettings and utilizes pydantic for managing
    environment variables and settings. It reads configurations from an `.env` file.

    Attributes:
        `model_config` (SettingsConfigDict): Configuration for the settings model.
        `host` (str): Hostname of the Redis server.
        `port` (int): Port number of the Redis server.
        `db` (int): Database number to connect to.
        `username` (str | None): Username for Redis authentication.
        `password` (str): Password for Redis authentication.
    """
    model_config = SettingsConfigDict(
        env_prefix="REDIS_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    host: str
    port: int
    db: int
    username: str | None = None
    password: str
    decode_responses: bool = True
