from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = "sqlite:///parents_database.db"

engine = create_engine(DATABASE_URI, echo=True)
# engine = create_engine(DATABASE_URI, echo=False)
Base = declarative_base()


# 1:N - jeden do wielu
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # maksymalna długość tekstu
    children = relationship("Child", backref='parent')
    # backref - tworzy pole parent w obiekcie klasy Child
    # parents = [ {"id":1, "name": "Radek", "children": []}]


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

    def __repr__(self):
        return f"id={self.id}, name={self.name}"


Base.metadata.create_all(engine)

Sesion = sessionmaker(bind=engine)
session = Sesion()

# parent = Parent(name="Rodzic")
# child1 = Child(name="Dziecko 1", parent=parent)
# child2 = Child(name="Dziecko 2", parent=parent)
#
# session.add_all(
#     [parent, child1, child2]
# )

# session.commit()

our_parent = session.query(Parent).all()
print(our_parent)  # [<__main__.Parent object at 0x104864440>]

our_parent_filtered = session.query(Parent).filter_by(name="Rodzic").first()
print(f"Rodzic: {our_parent_filtered.name}")  # Rodzic: Rodzic

children = our_parent_filtered.children
for child in children:
    print(f"Dziecko: {child.name}")
    print(f"Rodzic: {child.parent.name}")
# [<__main__.Parent object at 0x1069002f0>]
# Rodzic: Rodzic
# Dziecko: Dziecko 1
# Rodzic: Rodzic
# Dziecko: Dziecko 2
# Rodzic: Rodzic
# 2025-07-12 12:46:21,338 INFO sqlalchemy.engine.Engine SELECT parents.id AS parents_id, parents.name AS parents_name
# FROM parents
# WHERE parents.name = ?
#  LIMIT ? OFFSET ?
# 2025-07-12 12:46:21,338 INFO sqlalchemy.engine.Engine [generated in 0.00005s] ('Rodzic', 1, 0)
# Rodzic: Rodzic
# 2025-07-12 12:46:21,339 INFO sqlalchemy.engine.Engine SELECT children.id AS children_id, children.name AS children_name, children.parent_id AS children_parent_id
# FROM children
# WHERE ? = children.parent_id
