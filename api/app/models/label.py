from pydantic import BaseModel
import uuid

class Label(BaseModel):
    id: uuid.UUID
    name: str
