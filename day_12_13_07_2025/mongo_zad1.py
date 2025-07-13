# https://www.ovhcloud.com/pl/learn/what-is-mongodb/
# nosql - not only sql
# MongoDB to open-source'owa, dokumentowa baza danych typu NoSQL dostępna na różne platformy.
# Wykorzystuje format JSON z opcjonalnymi schematami i jest rozwijana przez MongoDB Inc.

# docker pull mongo
# docker run --name mongodb -d -p 27017:27017 mongo
# pip install --upgrade pymongo

import pymongo

my_client = pymongo.MongoClient("mongodb://localhost:27017")

my_db = my_client['mysatabase']
my_col = my_db['customers']

print(my_db.list_collection_names())
