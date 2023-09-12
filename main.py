from fastapi import FastAPI, status, Depends, HTTPException
from database import SessionLocal, engine
from models import Base, Users
from sqlalchemy.orm import Session
from schemas import User, ShowUser

# Create all tables in db
Base.metadata.create_all(bind=engine)

# app instance
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api", status_code=status.HTTP_201_CREATED)
def home(request: User, db: Session = Depends(get_db)):
    new_user = Users(username=request.username, email=request.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if not new_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"user not created")

    return new_user

@app.get("/api/{user_id}", response_model=ShowUser)
def fetch_one(user_id: int, db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The requested user is not found")
    return user