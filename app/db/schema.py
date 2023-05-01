from pydantic import BaseModel
from datetime import datetime

# * Схемы задач
class TasksBase(BaseModel):
    title: str | None
    description: str | None
    deadline: datetime | None
    user_id: int
    group_id: int
    created_at: datetime
    last_update: datetime
    status: str | None


class TasksCreate(TasksBase):
    pass


class Tasks(TasksBase):
    id: int
    is_deleted: datetime | None
    
    class Config:
        orm_mode = True
    

# * Схемы групп
class GroupsBase(BaseModel):
    title: str
    user_id: int

class GroupCreate(GroupsBase):
    pass


class Groups(GroupsBase):
    id: int
    tasks: list[Tasks] = []
    
    class Config:
        orm_mode = True


# * Схемы пользоватлея
class UserBase(BaseModel):
    email: str
    name: str
    

class UserCreate(UserBase):
    password: str


# ! изменить is_delited на дату, когда производится удаление.
# TODO: Реализовать backgroundtask для отчистки 
class User(UserBase):
    id: int
    is_deleted: datetime
    groups: list[Groups] = []
    tasks: list[Tasks] = []
    registered_at: datetime
    
    class Config:
        orm_mode = True