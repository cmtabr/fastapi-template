from fastapi import Depends, HTTPException, Response
from fastapi.routing import APIRouter

from api.models import Users
from api.schemas import UserLoginSchema
from api.utils import Logger, SessionManager, TokenHandler

_logger = Logger(__name__).logger

auth_router = APIRouter(
    prefix="/api/v1/auth", tags=["Auth"],
    )

@auth_router.post("/login")
async def login(
    login: UserLoginSchema,
    sm: SessionManager = Depends(SessionManager),
    th: TokenHandler = Depends(TokenHandler)
    ):
    try:
        with sm as session:
            user = session.query(Users).filter(
                Users.email==login.email,
                Users.password==login.password).first()
            if not user:
                _logger.error("User not found")
                raise HTTPException(status_code=403, detail="Resource not found")
            token = await th.create_token(user.user_id)
            headers = {
                "Key": "X-API-Key",
                "Authorization": token.with_typo
            }
            _logger.info("User logged in successfully")
        return Response(headers=headers, media_type="application/json")
    except Exception as e:
        _logger.error("Error logging in user: %s", e)
        raise HTTPException(status_code=403, detail="Resource not found")
