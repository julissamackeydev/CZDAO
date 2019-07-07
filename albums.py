from pymongo import MongoClient, DESCENDING
from datetime import date
import os

os.environ['CONNECTION_STRING']='mongodb+srv://czdao:Mon_0908@cz-rtjkk.mongodb.net/test?retryWrites=true'

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

albums = db.albums

def create_album(album_info):
	new_album = {
		"links": album_info['links'],
		"description": album_info['description']
	    }
	albums.insert_one(new_album)
	return

def get_albums():
	all_albums = []
	cursor = albums.find()
	for document in cursor:
		album = {
			"links": document['links'],
			"description": document['description']
			}
		all_albums.append(album)
	return all_albums

def get_album(description):
	albumRaw = albums.find_one({"description": description})
	album = {
		"links": albumRaw['links'],
		"description": albumRaw['description']
	}
	return album

if __name__ == "__main__":
    album_info = {
        "links": ["link1", "link2"],
        "description": "An Album"
        }
    create_album(album_info)

if __name__ == "__main__":
    # print(get_albums())
    pass