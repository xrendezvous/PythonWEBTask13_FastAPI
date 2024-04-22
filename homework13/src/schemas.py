from pydantic import BaseModel, EmailStr
from datetime import date


class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birthday: date
    additional_info: str = None


class ContactUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: EmailStr = None
    phone_number: str = None
    birthday: date = None
    additional_info: str = None


class ContactResponse(ContactCreate):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserInDB(UserCreate):
    hashed_password: str


class UserResponse(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None