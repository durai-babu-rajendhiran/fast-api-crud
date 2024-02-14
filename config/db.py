from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]

ITEM_COLLECTION = "items"
item_collection = db[ITEM_COLLECTION]
USERS_COLLECTION = "users"
users_collection = db[USERS_COLLECTION]