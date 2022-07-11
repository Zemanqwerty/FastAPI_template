from starlette.config import Config

config = Config('.env')

DATABASE_URL = config('FT_DATABASE_URL', cast=str, default='')

ACCESS_TOKEN_EXPIRE_MINUTES = 60

ALGORITHM = 'HS256'
SECRET_KEY = config(FT_SECRET_KEY, cast=str, default='4cdbd3402cfc34ab29e0f78f3a1f77ef8c21cf3f84ec67f6652ccbe02a29b03c')