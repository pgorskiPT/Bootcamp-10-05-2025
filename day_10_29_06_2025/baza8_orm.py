# ORM - Mapowanie obiektowo-relacyjne, to nowoczesne podejście do zagadnienia współpracy z bazą danych
# charakterystyczną cechą jest wykorzystywanie filozofii programowania obiektowego
# zamian obiektów na tabele w bazie danych

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# klasy odwzorowujące tabele - encje (model)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age}>"


# Podlaczamy bazę danych
# echo=True - pokaż logi bazy danych
engine = create_engine('sqlite:///mydatabase.db', echo=True)  # zwraca silnik
Base.metadata.create_all(engine)  # Tworzy tabele w bazie danych
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

# utworzenie obiektu sesji
# za pomocą sesji połaczymy sie i porozumiewamy z bazą
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
session.add(new_user)  # INSERT INTO users (name, age) VALUES (?, ?) ('Jan Kowalski', 30)

session.commit()
session.close()

users = session.query(User).all()
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
for user in users:
    print(user)
    print(f"Imie: {user.name} wiek: {user.age}")
# <User(name=Jan Kowalski, age=30>
# Imie: Jan Kowalski wiek: 30
# <User(name=Jan Kowalski, age=30>
# Imie: Jan Kowalski wiek: 30
# <User(name=Jan Kowalski, age=30>
# Imie: Jan Kowalski wiek: 30

result = session.execute(text("SELECT * FROM users"))
for row in result:
    print(row)
# (1, 'Jan Kowalski', 30)
# (2, 'Jan Kowalski', 30)
# (3, 'Jan Kowalski', 30)
# (4, 'Jan Kowalski', 30)

stmt = text("SELECT * FROM users")
users = session.query(User).from_statement(stmt).all()

for user in users:
    print(type(user))  # <class '__main__.User'>
    print(user.name)  # Jan Kowalski
# wywniku mamy obiekty
