from typing import Annotated
from fastapi import FastAPI, Depends
from db.db_setup import  get_db
from sqlalchemy.orm import Session
from api import bug_api


app = FastAPI()

db_dependency = Annotated[Session, Depends(get_db)]

app.include_router(bug_api.router)
