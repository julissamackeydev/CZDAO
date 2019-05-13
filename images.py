from pymongo import MongoClient, DESCENDING
from datetime import date
import os

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

images = db.images

def add_image(image):
	new_image = {
        "description": image['description'],
        "link": image['link']
    }
	images.insert_one(image)
	return

if __name__ == "__main__":
	image = {
		"description": "An image",
		"link": "Link"
		}
	# add_image(image)
	pass