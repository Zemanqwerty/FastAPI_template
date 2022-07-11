from datetime import datetime, timedelta
import hashlib
from jose import JWSError, jwt
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password: str, hashed_password :str) -> str:
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password

def create_access_tocken(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_tocken(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except JWSError:
        return None