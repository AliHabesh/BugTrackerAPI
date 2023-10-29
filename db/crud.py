from psycopg2 import IntegrityError
from sqlalchemy.orm import Session

from dtos.dto import BugData
from models.bug import Bug


def create_bug(db: Session, bug: BugData):
    new_bug = Bug(issued_by=bug.issued_by, status=bug.status, description=bug.description, assigned_to=bug.assigned_to)
    db.add(new_bug)
    db.commit()
    db.refresh(new_bug)
    return new_bug


def update_bug(db: Session, bug_id: int, updated_bug: BugData):
    try:
        db.query(Bug).filter(Bug.id == bug_id).update(vars(updated_bug))
        db.commit()
        existing_bug = db.query(Bug).get(bug_id)
        return existing_bug
    except IntegrityError:
        db.rollback()
        return None


def delete_bug(db: Session, bug_id: int):
    bug_to_delete = db.query(Bug).filter(Bug.id == bug_id).first()
    if bug_to_delete:
        db.delete(bug_to_delete)
        db.commit()
        return True  # Return True to indicate successful deletion
    else:
        return False  # Return False if bug with the given ID doesn't exist
