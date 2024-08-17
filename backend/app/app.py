from flask import Flask, request, jsonify, send_file
import os
from services.video_saver_service import VideoSaver

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_video():
    pass

@app.route('/')
def index():
    return "Welcome to the Video Transcription API!"

if __name__ == '__main__':
    app.run(debug=True)
