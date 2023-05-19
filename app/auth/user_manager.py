from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, IntegerIDMixin

from db.model import Users, get_user_db
from .auth import auth_backend

from config import SECRET_KEY



SECRET = SECRET_KEY


class UserManager(IntegerIDMixin, BaseUserManager[Users, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: Users, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: Users, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: Users, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
    async def on_after_login(
        self,
        user: Users,
        responce: Optional[Request] = None,
        request: Optional[Request] = None,
    ):
        print(f"User {user.id} logged in.")



async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
    
fastapi_users = FastAPIUsers[Users, int](get_user_manager, [auth_backend],)

current_active_user = fastapi_users.current_user(active=True)