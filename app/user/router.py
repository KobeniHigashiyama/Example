from fastapi import APIRouter, Depends, Response

from app.exceptions import (
    CannotAddDataToDatabase,
    UserAlreadyExistsException,
)
from app.user.auth import authenticate_user, create_access_token, get_password_hash
from app.user.dao import UserDao
from app.user.dependencies import get_current_user
from app.user.models import Users
from app.user.schemas import SUserRegister

router_auth = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

router_users = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router_auth.post("/register", status_code=201)
async def register_user(user_data: SUserRegister):
    existing_user = await UserDao.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    new_user = await UserDao.add(email=user_data.email, hashed_password=hashed_password)
    if not new_user:
        raise CannotAddDataToDatabase


@router_auth.post("/login")
async def login_user(response: Response, user_data: SUserRegister):
    user = await authenticate_user(user_data.email, user_data.password)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}


@router_auth.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router_users.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user





