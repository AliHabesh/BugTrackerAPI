from pydantic import BaseModel


class BugData(BaseModel):
    issued_by: str
    status: str
    description: str
    assigned_to: str
