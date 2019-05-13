from pymongo import MongoClient, DESCENDING
from datetime import date
import os

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

bio = db.bio
		
def get_bio():
	bioRaw = bio.find_one()
	current_bio = {
		"date": bioRaw['date'],
		"content": bioRaw['content']
		}
	return current_bio

def update_bio(text):
	bio.drop()
	new_bio = {
		"date": date.today().strftime('%m-%d-%Y'),
		"content": text['content']
		}
	bio.insert_one(new_bio)
	return    

if __name__ == "__main__":
    # update_bio('A biography, II') 
    # get_bio()   
	pass