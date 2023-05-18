from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page

from service.task import task_service

from db.schema import Task, TaskCreate


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/', response_model=Page[Task])
async def get_tasks(user_id: int = 0):
    result = task_service.get_tasks(user_id=user_id)
    return paginate(result)


@router.post('/', response_model=Task)    
async def create_task(task: TaskCreate):
    return task_service.create_task(task)


@router.get('/group/{group_id}', response_model=Page[Task])
async def get_tasks_in_group(group_id):
    result = task_service.get_tasks_in_group(group_id)
    return paginate(result)


@router.put('/update/{task_id}', response_model=Task)
async def udpate_task(task_id, task: Task):
    result = task_service.update_task(task_id, task)

    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "task_id": task_id, 
        })

    return {
        "task_id": task_id, 
        "status": "success!", 
        "result": result,
        }


@router.delete('/{task_id}')
async def delete_task(task_id: int):
    result = task_service.delete_task(task_id)

    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "task_id": task_id, 
        })

    return {"task_id": task_id, "status": "success!"}