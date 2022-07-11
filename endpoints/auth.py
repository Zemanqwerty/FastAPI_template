from cmath import log
from tkinter import N
from fastapi import APIRouter, Depends, HTTPException, status
from models.token import Login, Token
from repositories.users import UserRepository
from .depends import get_user_repository
from ..core.security import check_password


router = APIRouter()


@router.post('/', response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_username(username=login.username)
    if user is None or not check_password(login.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return
