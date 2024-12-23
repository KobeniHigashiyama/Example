from datetime import datetime

from fastapi import Request,  Depends
from jose import JWTError, jwt, ExpiredSignatureError
from app.config import settings
from app.user.dao import UserDao
from app.exceptions import (TokenExpiredException,
                            TokenAbsentException, IncorrectTokenFormatException,
                            UserIsNotPresentException)


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except ExpiredSignatureError:
        # Как позже выяснилось, ключ exp автоматически проверяется
        # командой jwt.decode, поэтому отдельно проверять это не нужно
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserIsNotPresentException
    user = await UserDao.find_one_or_none(id=int(user_id))
    if not user:
        raise UserIsNotPresentException
    return user
