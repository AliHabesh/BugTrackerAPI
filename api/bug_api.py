from typing import Annotated

from fastapi import Body, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from db import crud
from db.crud import delete_bug
from db.db_setup import get_db
from dtos.dto import BugData

router = APIRouter()


@router.post("/bugs/")
def create_bug(bug: Annotated[BugData, Body(embed=True)], db: Session = Depends(get_db)):
    return crud.create_bug(db, bug)


@router.put("/bugs/{bug_id}")
def update_bug(bug_id: int, updated_bug: Annotated[BugData, Body(embed=True)], db: Session = Depends(get_db)):
    result = update_bug(db, bug_id, updated_bug)
    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Bug not found")


@router.delete("/bugs/{bug_id}")
def delete_bug_endpoint(bug_id: int, db: Session = Depends(get_db)):
    deleted = delete_bug(db, bug_id)
    if deleted:
        return {"detail": "Bug deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Bug not found")
