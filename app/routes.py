from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'noisense'
app.config['MYSQL_DB'] = 'noisense'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status= "running")

@app.route('/add_recording', methods=['POST'])
def add_recording():
    try:
        audio_id = request.form['audio_id']
        audio_title = request.form['audio_title']
        audio_timestamp = request.form['audio_timestamp']
        audio_path = request.form['audio_path']
        audio_size = request.form['audio_size']
        audio_duration = request.form['audio_duration']

        cursor = mysql.connection.cursor()
        cursor.execute('''
            INSERT INTO recordings (audio_id, audio_title, audio_timestamp, audio_path, audio_size, audio_duration)
            VALUES (%s, %s, %s, %s, %s, %s)''', 
            (audio_id, audio_title, audio_timestamp, audio_path, audio_size, audio_duration)
        )
        mysql.connection.commit()
        return jsonify(status='success')
    except Exception as e:
        return jsonify(status='error', message=str(e))
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
