# CRUD - CREATE, READ, UPDATE, DELETE
# od wersji 2.0 sqlqlchemy podejście deklaratywne

from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import sqlalchemy

print(sqlalchemy.__version__)  # 2.0.41

DB_URL = "sqlite:///example_orm.db"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name!r}, email={self.email!r}"


# Tworzenie tabel
engine = create_engine(DB_URL, echo=False)
Base.metadata.create_all(engine)


def create_user(session: Session, name: str, email: str):
    session.add(User(name=name, email=email))


def get_users(session: Session):
    return session.query(User).all()


def update_email(session: Session, user_id: id, new_email: str):
    user = session.get(User, user_id)
    if user:
        user.email = new_email


def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user:
        session.delete(user)


# demo
def main():
    with Session(engine) as session:
        # create
        # create_user(session, "Margaret Hamilton", "margaret@nasa.gov")
        # create_user(session, "Linus Tornvalds", "linus@kernel.org")
        # session.commit()
        # ctrl / - komentarz

        # read
        print("== All users ==")
        print(get_users(session))

        # update
        update_email(session, 1, "margaret@apollo.guide")
        session.commit()
        print("\n== After email update ==")
        print(get_users(session))

        # delete
        delete_user(session, 2)
        session.commit()
        print("\n== After delete ==")
        print(get_users(session))


if __name__ == '__main__':
    main()
# == All users ==
# [User(id=1, name='Margaret Hamilton', email='margaret@nasa.gov', User(id=2, name='Linus Tornvalds', email='linus@kernel.org']
#
# == After email update ==
# [User(id=1, name='Margaret Hamilton', email='margaret@apollo.guide', User(id=2, name='Linus Tornvalds', email='linus@kernel.org']
# == After delete ==
# [User(id=1, name='Margaret Hamilton', email='margaret@apollo.guide']
# Przerwa 11:40
