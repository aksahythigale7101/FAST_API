from sqlmodel import select, Session

from app.models.user import User


def get_user_by_username(session: Session, username: str):
    Stmt = select(User).where(User.username == username)
    return session.exec(Stmt).first()


def get_user_by_email(session: Session, email: str):
    Stmt = select(User).where(User.email == email)
    return session.exec(Stmt).first()


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user





