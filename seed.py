from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://czdao:Mon_0908@cz-rtjkk.mongodb.net/test?retryWrites=true")
db = client.cz

albums = db.albums
bio = db.bio
content = db.content
events = db.events
images = db.images 

album = {
    "links": ["link"],
    "description": "hello world"
}

albums.insert_one(album)