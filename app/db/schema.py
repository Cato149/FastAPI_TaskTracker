from pydantic import BaseModel, EmailStr
from datetime import datetime

# * Схемы задач
class TaskBase(BaseModel):
    title: str | None
    description: str | None
    deadline: datetime | None
    user_id: int
    group_id: int
    created_at: datetime
    last_update: datetime
    status: str | None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    is_deleted: datetime | None
    
    class Config:
        orm_mode = True
    

# * Схемы групп
class GroupBase(BaseModel):
    title: str
    user_id: int

class GroupCreate(GroupBase):
    pass


class Group(GroupBase):
    id: int
    tasks: list[Task] = []
    
    class Config:
        orm_mode = True


# * Схемы пользоватлея
class UserBase(BaseModel):
    email: str
    name: EmailStr
    

class UserCreate(UserBase):
    password: str


# ! изменить is_delited на дату, когда производится удаление.
# TODO: Реализовать backgroundtask для отчистки 
class User(UserBase):
    id: int
    is_deleted: datetime
    groups: list[Group] = []
    tasks: list[Task] = []
    registered_at: datetime
    
    class Config:
        orm_mode = True