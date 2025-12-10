from pydantic import BaseModel
import uuid

class TaskLabel(BaseModel):
    task_id: uuid.UUID
    label_id: uuid.UUID
