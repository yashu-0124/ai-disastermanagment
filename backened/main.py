from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Request
from schemas import RequestCreate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Disaster Volunteer Network")


@app.get("/")
def home():
    return {
        "message": "AI Disaster Volunteer Network API Running"
    }


@app.post("/requests")
def create_request(data: RequestCreate, db: Session = Depends(get_db)):

    obj = Request(
        name=data.name,
        phone=data.phone,
        request_type=data.request_type,
        location=data.location,
        priority="Pending",
        status="Open"
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    return obj


@app.get("/requests")
def get_requests(db: Session = Depends(get_db)):
    return db.query(Request).all()
