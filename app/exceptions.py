

class APIException(Exception):
    def __init__(self, detail: str, status_code: int = 400, code: str = "API_ERROR"):
        self.detail = detail
        self.status_code = status_code
        self.code = code
        super().__init__(detail)

class TaskNotFoundError(APIException):
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found", status_code=404, code="TASK_NOT_FOUND")

class OwnerNotFoundError(APIException):
    def __init__(self, owner_id: int):
        self.owner_id = owner_id
        super().__init__(f"Owner with ID {owner_id} not found", status_code=404, code="OWNER_NOT_FOUND")

class OwnerInUseError(APIException):
    def __init__(self, owner_id: int):
        self.owner_id = owner_id
        super().__init__(f"Owner with ID {owner_id} is being used by a task", status_code=409, code="OWNER_IN_USE")