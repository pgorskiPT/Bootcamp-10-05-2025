from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from baza_krok1 import User, Post

# docker rm mysql_db - usuniecie kontenera

# docker run -d \
#   --name mysql_db \
#   -e MYSQL_ROOT_PASSWORD=abc123 \
#   -e MYSQL_DATABASE=zaawansowana_baza \
#   -p 3306:3306 \
#   mysql:8.0

DATABASE_URI = 'mysql+pymysql://root:abc123@localhost:3306/zaawansowana_baza'

engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = User(name="Jan Kowalski", email='jan.kowalski@wp.pl')
    session.add(new_user)

    new_post = Post(title="Pierwszy post", content='To jest treść pierwszego posta.', user=new_user)
    session.add(new_post)

    session.commit()
except Exception as e:
    print("Bład:", e)
    session.rollback()  # wycofanie zmian w przypadku błedu

finally:  # wykona się zawsze
    session.close()
