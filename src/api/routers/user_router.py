from fastapi.routing import APIRouter

user_router = APIRouter(
    prefix="/api/v1/user", tags=["User"]
    )

@user_router.get("/me")
async def get_current_user(): ...

@user_router.post("/create")
async def create_user(): ...

@user_router.put("/update")
async def update_user(): ...

@user_router.delete("/delete")
async def delete_user(): ...
