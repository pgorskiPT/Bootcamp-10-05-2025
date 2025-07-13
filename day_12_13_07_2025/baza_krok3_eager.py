from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, joinedload
from baza_krok1 import User, Post
from baza_krok2_transakcja import Session

# DATABASE_URI = 'mysql+pymysql://root:abc123@localhost:3306/zaawansowana_baza'

session = Session()
#
# users_with_posts = session.query(User).all()
#
# for user in users_with_posts:
#     print(f"Użytkownik: {user.name}")
#     for post in user.posts:
#         print(f"   Post: {post.title}")
# 2025-07-13 10:20:37,481 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email
# FROM users
# 2025-07-13 10:20:37,482 INFO sqlalchemy.engine.Engine [generated in 0.00006s] {}
# Użytkownik: Jan Kowalski
# 2025-07-13 10:20:37,483 INFO sqlalchemy.engine.Engine SELECT posts.id AS posts_id, posts.title AS posts_title, posts.content AS posts_content, posts.user_id AS posts_user_id
# FROM posts
# WHERE %(param_1)s = posts.user_id
# 2025-07-13 10:20:37,483 INFO sqlalchemy.engine.Engine [generated in 0.00005s] {'param_1': 1}
#    Post: Pierwszy post

# Problem N+1

users_with_posts = session.query(User).options(joinedload(User.posts)).all()
for user in users_with_posts:
    print(f"Użytkownik: {user.name}")
    for post in user.posts:
        print(f"   Post: {post.title}")
# 2025-07-13 10:23:47,069 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, posts_1.id AS posts_1_id, posts_1.title AS posts_1_title, posts_1.content AS posts_1_content, posts_1.user_id AS posts_1_user_id
# FROM users LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.user_id
# 2025-07-13 10:23:47,069 INFO sqlalchemy.engine.Engine [generated in 0.00011s] {}
# Użytkownik: Jan Kowalski
#    Post: Pierwszy post