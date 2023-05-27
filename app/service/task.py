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

        if not db_task:
            return None

        session.add(db_task)
        session.commit()

        return db_task

    def get_tasks_in_group(self, group_id: int):
        tasks = session.query(Tasks).filter(Tasks.group_id == group_id)

        if not tasks:
            return None

        return tasks

    def get_tasks(self, user_id: int):
        tasks = session.query(Tasks).filter(Tasks.user_id == user_id)

        if not tasks:
            return None

        return tasks

    def delete_task(self, task_id: int):
        """
        Можно использовать библиотеку schedule для удаления по расписанию 
        """
        delete_date = datetime.date.today() + datetime.timedelta(days=7)
        task = session.query(Tasks).filter(Tasks.id == task_id).first()

        if not task:
            return None

        task.update({Tasks.is_deleted: delete_date})
        session.commit()
        # return API != return Service - не выдавать клиентскую ошибку в сервисе!
        return True


# ! посмотреть что такое Mapper  в Python. Применить тут

    def update_task(self, task_id: int, updated_task: Task):
        task = session.query(Tasks).filter(Tasks.id == task_id).first()

        if not task:
            return None

        task.deadline = updated_task.deadline
        task.description = updated_task.description
        task.group_id = updated_task.group_id
        task.status = updated_task.status
        task.title = updated_task.title
        session.commit()
        session.refresh(task)
        return task


task_service = TaskService()