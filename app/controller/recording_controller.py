from flask import request, jsonify
from app.services.recording_service import RecordingService
from app import app

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status="running")

@app.route('/add_recording', methods=['POST'])
def add_recording():
    try:
        audio_id = request.form['audio_id']
        audio_title = request.form['audio_title']
        audio_timestamp = request.form['audio_timestamp']
        audio_path = request.form['audio_path']
        audio_size = request.form['audio_size']
        audio_duration = request.form['audio_duration']

        success, message = RecordingService.add_recording(
            audio_id, audio_title, audio_timestamp, audio_path, audio_size, audio_duration)

        if success:
            return jsonify(status='success', message=message, data={"audio_id": audio_id})
        else:
            return jsonify(status='error', message=message)
    except Exception as e:
        return jsonify(status='error', message=str(e))
