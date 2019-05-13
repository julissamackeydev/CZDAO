from flask import Flask, make_response, request, jsonify
import albums
import auth
import bio
import content
import events
import images
import user

app =Flask(__name__)

@app.route('/health-check', methods=['GET'])
def health_check():
    return 'Good to go'

@app.route('/login', methods=['POST'])
def login():	
	pass

@app.route('/create-album', methods=['POST'])
def create_album():
	albums.create_album(request.json)
	return make_response(jsonify({'success': True}), 200)

@app.route('/edit-bio', methods=['POST'])
def edit_bio():
	bio.update_bio(request.json) 
	return make_response(jsonify({'success': True}), 200)       

@app.route('/add-content', methods=['POST'])
def add_content():
	content.add_content(request.json)
	return make_response(jsonify({'success': True}), 200)

@app.route('/add-image', methods=['POST'])
def add_image():
	images.add_image(request.json)
	return make_response(jsonify({'success': True}), 200)

@app.route('/get-albums', methods=['GET'])
def get_albums():
	response = albums.get_albums()
	return make_response(jsonify({'success': True, 'albums': response}), 200)

@app.route('/get-album', methods=['GET'])
def get_album():
	response = albums.get_album(request.json['description'])
	return make_response(jsonify({'success': True, 'album': response}), 200)

@app.route('/get-bio', methods=['GET'])
def get_bio():
	response = bio.get_bio()
	return make_response(jsonify({'success': True, 'bio': response}), 200)	

@app.route('/get-events', methods=['GET'])
def get_events():
	response = events.get_events()
	return make_response(jsonify({'success': True, 'events': response}), 200)	

@app.route('/add-event', methods=['POST'])
def add_event():
	events.add_event(request.json)	
	return make_response(jsonify({'success': True}), 200)

@app.route('/get-latest', methods=['GET'])
def get_latest():
	response = content.get_latest()
	return make_response(jsonify({'success': True, 'content': response}), 200)	



app.run()    