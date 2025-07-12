from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URI = "sqlite:///sprawdzenie.db"
# DATABASE_URI = "postgresql://username:password@localhost/my_database"
DATABASE_URI = "postgresql://myuser:mypassword@localhost/mydatabase"

engine = create_engine(DATABASE_URI)
# engine = create_engine(DATABASE_URI, echo=True)  # echo=True - logowanie komend bazy danych
Base = declarative_base()


class User(Base):
    __tablename__ = "new_users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name="Anna", age=25)
user2 = User(name="Tomek", age=35)

session.add_all([user1, user2])
session.commit()

# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
users = session.query(User).all()
for user in users:
    print(f"id: {user.id}, name: {user.name}, age: {user.age}")

# update
user_to_update = session.query(User).filter_by(name="Anna").first()
user_to_update.age = 27
session.commit()

session.close()
