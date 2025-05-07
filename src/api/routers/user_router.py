from fastapi import Depends, HTTPException, Header, Response
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

from typing import Annotated
from uuid import uuid4

from api.models import Users
from api.schemas import CreateUserSchema, GetUserSchema
from api.utils import Logger, SessionManager, TokenHandler

_logger = Logger(__name__).logger

user_router = APIRouter(
    prefix="/api/v1/user", tags=["User"]
    )

@user_router.get("/me")
async def get_current_user(
    sm: Session = Depends(SessionManager),
    th: TokenHandler = Depends(TokenHandler),
    token: str = Header(...)
    )-> GetUserSchema:
    _logger.info("Fetching current user")
    try:
        token = await th.decode_token(token)
        with sm as session:
            user = session.query(Users).filter(Users.user_id == token["sub"]).first()
        return user
    except Exception as e:
        _logger.error("Error fetching current user: %s", e)
        raise HTTPException(status_code=403, detail="Resource not found")

@user_router.post("/create")
async def create_user(
    user: Annotated[CreateUserSchema, "User creation payload"],
    sm: Session = Depends(SessionManager)
    ):
    _logger.info("Creating user")
    try:
        with sm as session:
            new_user = Users(
                user_id=uuid4(),
                username=user.username,
                password=user.password,
                email=user.email
            )
            session.add(new_user)
            session.commit()
        headers = {
            "Location": f"/api/v1/user/{new_user.user_id}",
            "Message": "User created successfully"
        }
        return Response(headers=headers, status_code=201, media_type="application/json")
    except Exception as e:
        _logger.error("Error creating user: %s", e)
        raise HTTPException(status_code=400, detail="User creation failed")

@user_router.get("/{user_id}")
async def get_user_by_id(
    user_id: str,
    sm: Session = Depends(SessionManager)
    ) -> GetUserSchema:
    _logger.info("Fetching user with ID: %s", user_id)
    try:
        with sm as session:
            user = session.query(Users).filter(Users.user_id == user_id).first()
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        _logger.error("Error fetching user: %s", e)
        raise HTTPException(status_code=404, detail="Unidentified resource")

@user_router.delete("/delete")
async def delete_user(): ...
