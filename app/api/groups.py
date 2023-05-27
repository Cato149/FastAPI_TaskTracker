from fastapi import APIRouter, HTTPException, status
from fastapi_pagination.ext.sqlalchemy import paginate
from fastapi_pagination import Page

from service.gruop import group_service

from db.schema import Group, GroupCreate, GroupUpdate


router = APIRouter(prefix='/group', tags=['group'])

# TODO тербует доработки
@router.get('/', response_model=Page[Group])
async def get_groups(user_id: int):
    result = group_service.get_groups(user_id)

    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "user_id": user_id,
        })

    return {
        "status": "success!",
        "result": paginate(result),
    }

# TODO тербует доработки
@router.post('/')
async def create_group(group: GroupCreate):
    result = group_service.create_group(group)

    if not result:
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail={
            "group": group,
        })

    return {
        "status": "success!",
        "result": result,
    }


@router.put('/add_task/{group_id}')
async def add_tasks_in_group(group_id: int, tasks_id: list[int]):
    result = group_service.add_tasks_in_group(group_id, tasks_id)

    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "user_id": group_id,
            "tasks_id": tasks_id,
        })

    return {
        "status": "success!",
        "result": result,
    }


@router.put('/update_name/{group_id}')
async def update_group_name(group_id: int, new_group: GroupUpdate):
    result = group_service.update_group_name(group_id, new_group)

    if not result:
        return HTTPException(status.HTTP_404_NOT_FOUND, detail={
            "group_id": group_id,
            "new_group": new_group,
        })

    return {
        "status": "success!",
        "result": result,
    }


@router.delete('/delete/{group_id}')
async def delete_group(group_id: int):
    result = group_service.delete_group(group_id)

    if not result:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={
            "user_id": group_id,
        })

    return {
        "status": "success!",
        "result": result,
    }
