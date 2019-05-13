from pymongo import MongoClient
from datetime import date
import os

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

users = db.users

def add_user(user):
    pass