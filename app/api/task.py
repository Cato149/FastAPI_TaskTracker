from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page

from service.task import task_service

from db.schema import Tasks, TasksCreate


router = APIRouter(prefix='/task', tags=['task'])



@router.get('/', response_model=Page[Tasks])
def get_tasks(user_id: int = 0):
    items = task_service.get_tasks(user_id=user_id)
    return paginate(items)


@router.post('/', response_model=Tasks)    
def create_task(task: TasksCreate):
    return task_service.create_task(task)


@router.get('/group/{group_id}', response_model=Page[Tasks])
def get_tasks_in_group(group_id):
    items = task_service.get_tasks_in_group(group_id)
    return paginate(items)


@router.post('/{task_id}')
def udpate_task(task_id):
    pass


@router.delete('/{task_id}')
def delete_task(task_id: int):
    return task_service.delete_task(task_id)