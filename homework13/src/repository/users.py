from sqlalchemy.orm import Session
from src.database.models import User
from fastapi import HTTPException


def update_avatar(email: str, avatar_url: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.avatar_url = avatar_url
        db.commit()
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
