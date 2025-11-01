from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    last_name: str

class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=72)

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    name: str | None = None
    last_name: str | None = None

    model_config = ConfigDict(from_attributes=True)
    
class VerifyEmail(BaseModel):
    email : str

class VerifyUser(BaseModel):
    username : str
    

class UserLogin(BaseModel):
    email: str
    password: str

class UserPublic(BaseModel):
    id: int
    username: str
    email: str
    name: str
    last_name: str
    model_config = ConfigDict(from_attributes=True)

class ListUsers(BaseModel):
    users: list[UserPublic]
    count: int

