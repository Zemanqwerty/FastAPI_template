from datetime import datetime
from .base import BaseRepository
from typing import List, Optional
from db.users import users
from models.users import User, UserIn
from core.security import hash_password

class UserRepository(BaseRepository):
    
    # GET ALL USERS LIST
    async def get_all(self) -> List[User]:
        query = users.select().with_only_columns([users.c.id_user, users.c.username])
        return await self.database.fetch_all(query=query)

    # ----------------

    # GET USER BY ID
    async def get_by_id(self, id: int) -> Optional[User]:
        query = users.select().where(users.c.id_user==id).with_only_columns(
            [users.c.id_user, users.c.username]
        )
        user = await self.database.fetch_one(query=query)

        if user is None:
            return None
        return user

    # ----------------

    # GET USER BY USERNAME
    async def get_by_username(self, username: str) -> Optional[User]:
        query = users.select().where(users.c.username==username)
        user = await self.database.fetch_one(query=query)

        if user is None:
            return None
        return user

    # ----------------

    # CREATE NEW USER
    async def create(self, user_data: UserIn) -> User:
        user = User(
            username = user_data.username,
            hashed_password = hash_password(user_data.password),
            created_at = datetime.utcnow(),
        )

        values = {**user.dict()}
        values.pop('id_user', None)

        query = users.insert().values(**values)
        try:
            user.id_user = await self.database.execute(query)
            return {'id_user': user.id_user, 'username': user.username}
        except:
            return {'message': f'user {user_data.username} already registered'}