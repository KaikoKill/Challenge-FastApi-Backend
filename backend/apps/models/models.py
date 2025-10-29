from pydantic import BaseModel
from datetime import datetime

class DeleteMixIn():
    @property
    def is_deleted(self):
        return self._is_delted
    def set_deleted(self,is_del:bool):
        self._is_delted=is_del


class User(BaseModel,DeleteMixIn):
    pass

class TimeStampMixIn():
    @property
    def created_at(self):
        self._created_at= datetime.now()
    @property
    def updated_at(self):
        self._updated_at=datetime.now()


class User(BaseModel):
    id : str
    username : str
    email : str
    created_at : datetime
    updated_at : datetime
    is_deleted=False

