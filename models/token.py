from pydantic import BaseModel

class Token(BaseModel):
    access_string: str
    token_type: str

class Login(BaseModel):
    username: str
    password: str