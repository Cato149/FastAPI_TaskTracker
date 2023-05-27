from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page

from service.task import task_service

from db.schema import Task, TaskCreate


router = APIRouter(prefix='/task', tags=['task'])

# TODO тербует доработки
@router.get('/', response_model=Page[Task])
async def get_tasks(user_id: int = 0):
    result = task_service.get_tasks(user_id=user_id)
    
    if not result: 
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "user_id": user_id,
        })
        
    return {
        "status": "success",
        "result": paginate(result),
        }

# TODO тербует доработки
@router.post('/', response_model=TaskCreate)    
async def create_task(task: TaskCreate):
    result = task_service.create_task(task)

    if not result:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={
            "task": task,
        })
        
    return task
    
# TODO тербует доработки
@router.get('/group/{group_id}', response_model=Page[Task])
async def get_tasks_in_group(group_id):
    result = task_service.get_tasks_in_group(group_id)
    
    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "group_id": group_id,
        })
        
    return {
        "status": "success!",
        "tasks": paginate(result),
        }


@router.put('/update/{task_id}')
async def udpate_task(task_id, task: Task):
    result = task_service.update_task(task_id, task)

    if not result:
        print('ok')
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

    return {
        "task_id": task_id, 
        "status": "success!",
        "result": result,
        }