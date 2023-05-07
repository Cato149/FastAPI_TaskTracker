import datetime
from db.schema import TaskCreate, Task
from db.model import Tasks
from db.database import session


class TaskService:
    def __init__(self) -> None:
        pass

    # * CRUD задачи
    def create_task(self, tasks: TaskCreate):
        db_task = Tasks(
            title=tasks.title,
            description=tasks.description,
            deadline=tasks.deadline,
            group_id=tasks.group_id,
            user_id=tasks.user_id,
            last_update=tasks.last_update,
            created_at=tasks.created_at,
            status=tasks.status)
        session.add(db_task)
        session.commit()
        return db_task

    def get_tasks_in_group(self, group_id: int):
        return session.query(Tasks).filter(Tasks.group_id == group_id)

    def get_tasks(self, user_id: int):
        return session.query(Tasks).filter(Tasks.user_id == user_id)

    def delete_task(self, task_id: int):
        delete_date = datetime.date.today() + datetime.timedelta(days=7)
        task = session.query(Tasks).filter(Tasks.id == task_id)

        task.update({Tasks.is_deleted: delete_date})
        session.commit()
        return {"message": "Task moved to trash. After 7 days it would be deleted permanently!"}

    def update_task(self, task_id: int, updated_task: Task):
        task = session.query(Tasks).filter(Tasks.id == task_id).first()
        
        task.deadline = updated_task.deadline
        task.description = updated_task.description
        task.group_id = updated_task.group_id
        task.status = updated_task.status
        task.title = updated_task.title
        session.commit()
        session.refresh(task)
        return task
        
        

task_service = TaskService()
