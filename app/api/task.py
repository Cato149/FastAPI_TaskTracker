from fastapi import APIRouter
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page

from service.task import task_service

from db.schema import Task, TaskCreate


router = APIRouter(prefix='/task', tags=['task'])



@router.get('/', response_model=Page[Task])
def get_tasks(user_id: int = 0):
    items = task_service.get_tasks(user_id=user_id)
    return paginate(items)


@router.post('/', response_model=Task)    
def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.get('/group/{group_id}', response_model=Page[Task])
def get_tasks_in_group(group_id):
    items = task_service.get_tasks_in_group(group_id)
    return paginate(items)


@router.put('/update/{task_id}', response_model=Task)
def udpate_task(task_id, task: Task):
    return task_service.update_task(task_id, task)


@router.delete('/{task_id}')
def delete_task(task_id: int):
    return task_service.delete_task(task_id)