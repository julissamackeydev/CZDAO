from pymongo import MongoClient, DESCENDING
from datetime import date
import os

client = MongoClient(os.environ['CONNECTION_STRING'])
db = client.cz

events = db.events

def get_events():
	all_events = []
	cursor = events.find()
	for document in cursor:
		event = {
			"description": document['description'],
			"date": document['date'],
			"location": document['location'],
			"city": document['city'],
			"event": document['event'],
			"tickets": document['tickets']
		}
		all_events.append(event)
	return all_events

def get_event(event_description):
	eventRaw = events.find_one({"event":event_description})
	event = {
		"description": eventRaw['description'],
		"date": eventRaw['date'],
		"location": eventRaw['location'],
		"city": eventRaw['city'],
		"event": eventRaw['event'],
		"tickets": eventRaw['tickets']
	}
	return event

def add_event(event):
	new_event =	{
	    "date": event['date'],
    	"location": event['location'],
    	"city": event['city'],
    	"event": event['event'],
    	"tickets": event['tickets']
		}
	events.insert_one(new_event)	
	return

if __name__ == "__main__":
	event = {
	    "date": "05-12-2019",
    	"location": "Concert Hall",
    	"city": "European City",
    	"event": "Concert",
    	"tickets": "Link"
		}
	# add_event(event)	
	# print(get_events())
	# print(get_event(event['event']))
	pass