from app.models.recording_model import Recording
from app import mysql

class RecordingService:
    @staticmethod
    def add_recording(audio_id, audio_title, audio_timestamp, audio_path, audio_size, audio_duration):
        try:
            recording = Recording(
                audio_id=audio_id,
                audio_title=audio_title,
                audio_timestamp=audio_timestamp,
                audio_path=audio_path,
                audio_size=audio_size,
                audio_duration=audio_duration
            )

            cursor = mysql.connection.cursor()
            cursor.execute('''
                INSERT INTO recordings (audio_id, audio_title, audio_timestamp, audio_path, audio_size, audio_duration)
                VALUES (%s, %s, %s, %s, %s, %s)''', 
                (recording.audio_id, recording.audio_title, recording.audio_timestamp, recording.audio_path,
                recording.audio_size, recording.audio_duration)
            )
            mysql.connection.commit()
            return True, "Data successfully added."
        except Exception as e:
            return False, str(e)
