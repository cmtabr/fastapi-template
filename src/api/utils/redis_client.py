from redis.asyncio import Redis

from api.config import RedisSettings
from api.utils import Logger

_redis_settings = RedisSettings()

_logger = Logger(__name__).logger


class RedisClient:
    def __init__(self) -> None:
        self.client = Redis(
            host=_redis_settings.host,
            port=_redis_settings.port,
            db=_redis_settings.db,
            username=_redis_settings.username,
            password=_redis_settings.password,
            decode_responses=_redis_settings.decode_responses
        )

    async def cache_refresh_token(self, jti: str, token: str) -> None:
        try:
            await self.client.set(name=jti, value=token, ex=60 * 60)
            _logger.info("Refresh token cached successfully")
        except Exception as e:
            _logger.error("Error caching refresh token: %s", e)
            raise e

    async def get_cached_refresh_token(self, jti: str) -> str | None:
        try:
            cached_token = await self.client.get(name=jti)
            if cached_token:
                _logger.info("Cached refresh token retrieved successfully")
                return cached_token
            else:
                _logger.warning("No cached refresh token found")
                return None
        except Exception as e:
            _logger.error("Error retrieving cached refresh token: %s", e)
            raise e

    async def delete_cached_refresh_token(self, jti: str) -> None:
        try:
            await self.client.delete(name=jti)
            _logger.info("Cached refresh token deleted successfully")
        except Exception as e:
            _logger.error("Error deleting cached refresh token: %s", e)
            raise e
