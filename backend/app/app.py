from flask import Flask, request, jsonify
from utils.transcript_video import transcript
import os

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_video():
  video_file = request.form.get('video_file')
  if not video_file:
    return jsonify({'error': 'No video file provided'}), 400

  try:
    video_path = os.path.join('videos', video_file)
    filename, tran = transcript(video_path)
    return jsonify({'filename': filename, 'transcription': tran}), 200
  except Exception as e:
    return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return "Welcome to the Video Transcription API!"

if __name__ == '__main__':
    app.run(debug=True)
