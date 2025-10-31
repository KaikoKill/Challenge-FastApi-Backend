from sqlalchemy.orm import Session
from sqlalchemy import select, func
from ..models.schemas import *
from ..models.models import User
from ..conf.security import get_password_hash, verify_password

def create_user(db: Session, user_create: UserCreate) -> User:
    db_user = User(
        username=user_create.username,
        email=user_create.email,
        name=user_create.name,
        last_name=user_create.last_name,
        password=get_password_hash(user_create.password)
    )
    db.add(db_user)
    db.commit()
    return db_user

def update_user(db: Session, user_db: User, user_update: UserBase) -> User:
    update_data = user_update.model_dump(exclude_unset=True)
    data = update_data.items()

    if "password" in update_data and update_data["password"]:
        hashed_password = get_password_hash(update_data["password"])
        update_data["password"] = hashed_password

    for key, value in data:
        setattr(user_db, key, value)

    db.add(user_db)
    db.commit()
    return user_db

def delete_user(db:Session, user_db: User, user_delete: UserById ):
    stmt = select(User).where(User.id == user_delete)
    result = db.execute(stmt)
    user = result.scalar_one()
    user["is_deleted"] = True
    return {
        "User_Delete": user
    }

def get_user_by_id(db:Session, user_id: UserById):
    stmt = select(User).where(User.id == user_id)
    result = db.execute(stmt)
    user = result.scalar_one()
    return {
        "User": user
    }

def get_users(db:Session):
    stmt = select(User).where(User.is_deleted == False)
    result = db.execute(stmt)
    
    users = result.scalars().all()
    count = db.query(func.count(User.id)).filter(User.is_deleted == False).scalar()
    count_deleted = db.query(func.count(User.id)).filter(User.is_deleted == True).scalar()
    
    return {
        "users":users,
        "count": count,
        "count_deleted":count_deleted
    }


def get_user_by_email(db : Session, email: str) -> User | None:
    stmt = select(User).where(User.email == email)
    result = db.execute(stmt).one()
    return result

def authenticate(db: Session, email: str, password: str) -> User | None:
    db_user = get_user_by_email(db, email)
    if not db_user:
        return None
    if not verify_password(password, db_user.hashed_password):
        return None
    return db_user
