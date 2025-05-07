from fastapi import Header, HTTPException
from jwt import decode, encode

from datetime import datetime, timedelta

from api.config import AuthSettings
from api.schemas import TokenSchema
from .logger import Logger

_logger = Logger(logger_name=__name__).logger

_auth_settings = AuthSettings()  # Load settings once at the module level


class TokenHandler:
    def __init__(self):
        """
        TokenHandler is a class that handles JWT token creation and decoding
        """
        self.secret = _auth_settings.secret
        self.algorithm = _auth_settings.algorithm

    async def create_token(self, user_id: str) -> TokenSchema:
        try:
            payload = {
                'sub': user_id,
                'exp': datetime.now() + timedelta(seconds=300)
            }
            token = encode(payload, self.secret, algorithm=self.algorithm)
            return TokenSchema(value=token)
        except Exception as e:
            _logger.error(f"Error creating token: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="Internal server error",
                headers={"X-Error": "Token creation failed"}
            )

    async def decode_token(self, token: str) -> dict:
        try:
            _logger.info(f"Decoding token: {token}")
            if not "Bearer" in token:
                _logger.error("Invalid token format")
                raise HTTPException(
                    status_code=403,
                    detail="Invalid token format",
                    headers={"X-Error": "Token format is invalid"}
                )
            token = token.split(" ")[1]
            payload = decode(token, self.secret, algorithms=self.algorithm)
            return payload
        except Exception as e:
            _logger.error(f"Error decoding token: {str(e)}")
            raise HTTPException(
                status_code=403,
                detail="Invalid token",
                headers={"X-Error": "Token decoding failed"}
            )
