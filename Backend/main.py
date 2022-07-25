from fastapi import FastAPI
from database import SessionLocal,engine
import models,schemas

models.Base.metadata.create_all(bing=engine)

app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()