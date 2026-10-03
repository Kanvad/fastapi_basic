from app.data import tasks


def create(task: dict):
    task["id"] = max(
        (item["id"] for item in tasks),
        default=0,
    ) + 1

    tasks.append(task)

    return task


def delete(task: dict):
    tasks.remove(task)

def get_all():
    return tasks

def get_completed():
    return [task for task in tasks if task["completed"]]

def update(task: dict, title: str, completed: bool):
    task["title"] = title
    task["completed"] = completed
    return task

def patch(task: dict, title: str | None = None, completed: bool | None = None):
    task["title"] = title if title is not None else task["title"]
    task["completed"] = completed if completed is not None else task["completed"]
    return task

def get_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None