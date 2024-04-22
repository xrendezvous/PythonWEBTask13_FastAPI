from sqlalchemy.orm import Session
from src.database.models import Contact
from src.schemas import ContactCreate, ContactUpdate
from sqlalchemy import or_, func, tuple_
from datetime import date, timedelta


def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def get_contacts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Contact).offset(skip).limit(limit).all()


def create_contact(db: Session, contact_data: ContactCreate):
    contact = Contact(
        first_name=contact_data.first_name,
        last_name=contact_data.last_name,
        email=contact_data.email,
        phone_number=contact_data.phone_number,
        birthday=contact_data.birthday,
        additional_info=contact_data.additional_info
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def update_contact(db: Session, contact_id: int, contact_data: ContactUpdate):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact_data_dict = contact_data.dict(exclude_unset=True)
        for key, value in contact_data_dict.items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact


def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return True
    return False


def get_contacts_by_search(db: Session, query: str):
    return db.query(Contact).filter(
        or_(
            Contact.first_name.ilike(f'%{query}%'),
            Contact.last_name.ilike(f'%{query}%'),
            Contact.email.ilike(f'%{query}%')
        )
    ).all()


def get_birthdays(db: Session):
    today = date.today()
    seven_days = [today + timedelta(days=i) for i in range(8)]
    birthdays = db.query(Contact).filter(
        tuple_(func.extract('month', Contact.birthday), func.extract('day', Contact.birthday)).in_(
            [(d.month, d.day) for d in seven_days]
        )
    ).all()
    return birthdays

