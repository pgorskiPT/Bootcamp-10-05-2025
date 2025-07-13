# https://www.mongodb.com/
import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# pip install pymongo

uri = ""

# client = MongoClient(uri, server_api=ServerApi('1'))  # [SSL: CERTIFICATE_VERIFY_FAILED]
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You succesfully connected to MongoDB")
except Exception as e:
    print("Error:", e)
# Pinged your deployment. You succesfully connected to MongoDB
#
# Process finished with exit code 0
