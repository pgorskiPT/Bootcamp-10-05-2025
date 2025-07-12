# relacje w bazach danych
from email_validator.rfc_constants import ATEXT_INTL_DOT_RE
# typy relacji:
# jeden do jednego - Obydwie tabele mogą zawierać jeden rekord po kazdej stronie
# # Każda wartość klucza podstawowego dotyczy tylko jednego lub nie dotyczy żadnego rekordu w tabeli powiązanej.
# # Relacje "jeden do jednego" są w większości wymuszane przez reguły biznesowe i nie wynikają w sposób naturalny z danych.
# # Jeśli taka reguła nie obowiązuje, możliwe jest łączenie obydwu tabel bez naruszania reguł normalizacji.

# jeden do wielu - tabele klucza podstawowowego zawiera tylko jeden rekord

# wiele do wielu - kazdy rekord obydwu tabel mozę odnośić się do dowolnej liczby rekordów
# # W przypadku takich relacji wymagana jest trzecia tabela nazywana tabelą powiązań,
# # ponieważ systemy relacyjne nie mogą bezpośrednio obsługiwać takiej relacji.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = "sqlite:///adress_book.db"

# engine = create_engine(DATABASE_URI, echo=True)
engine = create_engine(DATABASE_URI, echo=False)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates='addresses')

    def __repr__(self):
        return self.email


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin', age=38)

anakin1 = Person(name="Anakin Anakin", age=38)
anakin1.addresses = [Address(email='anakin@wp.pl')]

obi = Person(name='Obi Wan Kenobi', age=45)
obi.addresses = [
    Address(email='obi@example.com'),
    Address(email='waaka@wp.pl')
]

chewee = Person(name="Chewbacca", age=190)
chewee.addresses = [
    Address(email='chewbacca@example.com'),
    Address(email='chewee@wp.pl')
]

session.add(anakin)

# cascade=all - zapisało i obiekt Person i obiekt Address przypisany do tego Person
session.add(anakin1)
session.add(obi)
session.add(chewee)

session.commit()

all_ = session.query(Person).all()
print(all_)

# [Anakin (id=1), Anakin (id=2), Anakin Anakin (id=3), Anakin (id=4), Anakin Anakin (id=5),
# Obi Wan Kenobi (id=6), Chewbacca (id=7), Anakin (id=8), Anakin Anakin (id=9),
# Obi Wan Kenobi (id=10), Chewbacca (id=11), Anakin (id=12), Anakin Anakin (id=13),
# Obi Wan Kenobi (id=14), Chewbacca (id=15)]

first = session.query(Person).first()
print(first)  # Anakin (id=1)
print(type(first))  # <class '__main__.Person'>
print(first.name, first.age)  # Anakin 38

obi_list = session.query(Person).filter(
    Person.name.like('Obi%')  # WHERE person.name LIKE ?
).all()

print(obi_list)
# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
# WHERE person.name LIKE ?
# 2025-07-12 14:26:46,989 INFO sqlalchemy.engine.Engine [generated in 0.00006s] ('Obi%',)

chwee_list = session.query(Person).filter(
    Person.name.like('Che%')
).all()

print(chwee_list)
# [Chewbacca (id=7), Chewbacca (id=11), Chewbacca (id=15), Chewbacca (id=19), Chewbacca (id=23),
# Chewbacca (id=27), Chewbacca (id=31), Chewbacca (id=35)]

for chwwee in chwee_list:
    print(f"{chwwee.id=}, {chwwee.name=}, {chwwee.addresses=}")
# chwwee.id=7, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=11, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=15, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=19, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=23, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=27, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=31, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=35, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
# chwwee.id=39, chwwee.name='Chewbacca', chwwee.addresses=[chewbacca@example.com, chewee@wp.pl]
