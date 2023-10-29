# This is a sample Python script.
from typing import Annotated

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI, Depends, Body
from dtos.dto import BugData

from db.db_setup import SessionLocal
from sqlalchemy.orm import Session
from db import crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/bugs/")
def create_bug(bug: Annotated[BugData, Body(embed=True)], db: Session = Depends(get_db)):
    return crud.create_bug(db, bug)
