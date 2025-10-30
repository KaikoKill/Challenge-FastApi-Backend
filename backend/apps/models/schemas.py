from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    last_name: str
class UserCreate(UserBase):
    password : str
    
class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
class User_exists(BaseModel):
    username : str
    email : str

class VerifyUser(BaseModel):
    username : str
    

class UserLogin(BaseModel):
    username: str
    password: str
