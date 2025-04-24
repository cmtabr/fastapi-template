from fastapi import Depends, HTTPException, Response
from fastapi.routing import APIRouter
from models import Users
from schemas import UserLoginSchema, TokenHeaderSchema
from utils import Logger, SessionManager, TokenHandler

_logger = Logger(__name__).logger

auth_router = APIRouter(
    prefix="/api/v1/auth", tags=["Auth"],
    )

@auth_router.post("/login")
async def login(
    login_data: UserLoginSchema,
    sm: SessionManager = Depends(SessionManager),
    th: TokenHandler = Depends(TokenHandler)
    ):
    """
    Login endpoint
    """
    with sm as session:
        user = session.query(Users).filter(
            Users.email==login_data.email,
            Users.password_hash==login_data.password).first()
        if not user:
            _logger.error("User not found")
            raise HTTPException(status_code=403, detail="Resource not found")
        token = await th.create_token(user.user_id)
        headers = {"Key": token.key, "Authorization": token.with_typo}
        _logger.info("User logged in successfully: %s", headers) 
    return Response(headers=headers, media_type="application/json")

