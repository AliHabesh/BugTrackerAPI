from sqlalchemy.orm import Session

from dtos.dto import BugData
from models.bug import Bug


def create_bug(db: Session, bug: BugData):
    new_bug = Bug(issued_by=bug.issued_by, status=bug.status, description=bug.description, assigned_to=bug.assigned_to)
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug
