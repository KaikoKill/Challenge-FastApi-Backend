from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    last_name: str

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=72)
    
class VerifyEmail(BaseModel):
    email : str

class VerifyUser(BaseModel):
    username : str
    

class UserLogin(BaseModel):
    username: str
    password: str

class UserPublic(BaseModel):
    id: int
    username: str
    email: str
    name: str
    last_name: str

class ListUsers(BaseModel):
    users: list[UserPublic]
    count: int

class UserById(BaseModel):
    id: int