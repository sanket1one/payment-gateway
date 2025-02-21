from pydantic import EmailStr, BaseModel
from typing import Union

class UserInCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

# when we query the user
class UserOutput(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr

# Update the user 
class UserIsUpdate(BaseModel):
    id: int
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    email: Union[EmailStr, None] = None 
    password: Union[str, None] = None

# During the login
class UserInLogin(BaseModel):
    email: EmailStr
    password: str

# Providing the token
class UserWithToken(BaseModel):
    token: str