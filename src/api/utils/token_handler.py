from fastapi import Header, HTTPException
from jwt import decode, encode

from datetime import datetime, timedelta
from typing import Annotated

from config import AuthSettings
from schemas import TokenHeaderSchema
from .logger import Logger

_logger = Logger(logger_name=__name__).logger


class TokenHandler(AuthSettings):
    def __init__(self):
        """
        TokenHandler is a class that handles JWT token creation and decoding
        """
        super().__init__()

    async def create_token(self, user_id: str) -> TokenHeaderSchema:
        try:
            payload = {
                'user_id': user_id,
                'exp': datetime.now() + timedelta(seconds=300)
            }
            token = encode(payload, self.secret, algorithm=self.algorithm)
            return TokenHeaderSchema(key="X-Key", value=token)
        except Exception as e:
            _logger.error(f"Error creating token: {str(e)}")
            raise

    async def decode_token(self, token: Annotated[TokenHeaderSchema, Header()]) -> dict:
        try:
            payload: dict = decode(token.value, self.secret, algorithms=self.algorithm)
            return payload
        except Exception as e:
            _logger.error(f"Error decoding token: {str(e)}")
            raise
