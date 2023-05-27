import datetime
from db.model import Tasks
from db.schema import GroupCreate, Group, GroupUpdate
from db.model import Groups
from db.database import session


class GroupService:
    def __init__(self) -> None:
        pass

    def create_group(self, group: GroupCreate):
        db_group = Groups(
            title = group.title,
            user_id = group.user_id
            )
        
        if not db_group:
            return False
        
        session.add(db_group)
        session.commit()

        return db_group
    

    def add_tasks_in_group(self, group_id: int, tasks: list):
        group = session.query(Groups).filter(Groups.id == group_id).first()
        
        if not group:
            return None

        for task_id in tasks:
            task = session.query(Tasks).filter(Tasks.id == task_id).first()
            
            if not task:
                return None
            
            task.group_id = group_id
            
        session.commit()
        
        return True
    

    def get_groups(self, user_id: int):
        groups = session.query(Groups).filter(Groups.user_id == user_id)
        
        if not groups:
            return False
        
        return groups
    

    def delete_group(self, group_id: int):
        group = session.query(Groups).filter(Groups.id == group_id).first()

        if not group:
            return False
        
        group.delete()
        session.commit()
        # return API != return Service - не выдавать клиентскую ошибку в сервисе!
        return True
    

# ! посмотреть что такое Mapper  в Python. Применить тут
    def update_group_name(self, task_id: int, updated_group: GroupUpdate):
        group = session.query(Groups).filter(Groups.id == task_id).first()

        if not group:
            return None

        group.title = updated_group.title
        session.commit()
        session.refresh(group)
        return group


group_service = GroupService()