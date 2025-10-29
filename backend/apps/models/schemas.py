from pydantic import BaseModel

class User_exists(BaseModel):
    username : str
    email : str

class VerifyUser(BaseModel):
    username : str
    
class UserCreate(BaseModel):
    password : str

class UserLogin(BaseModel):
    username: str
    password: str
