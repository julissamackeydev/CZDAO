from pymongo import MongoClient, DESCENDING
from datetime import date
import os

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

content = db.content

def get_latest():
	latest = []
	cursor = content.find()
	for document in cursor:
		latestModel = {
			"descrption": document['description'],
			"date": document['date'],
			"content": document['content']
		}
		latest.append(latestModel)
	return latest	

def add_content(news):
	new_content = {
		"description": news['description'],
		"date": news['date'],
		"content": news['content']
		}
	content.insert_one(new_content)
	return

if __name__ == "__main__":
	news = {
		"description": "A news event",
		"date": "05-12-2018",
		"content": "This artist is doing this thing at a place."
		}
	# add_content(news)
	print(get_latest())
