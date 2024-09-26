from flask import Flask, render_template, send_file, request, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from services.transcription_service import transcript_video_service
from services.video_saver_service import VideoSaver

# Initialize Flask app
base_dir = Path.cwd()
input_dir = base_dir / "input"
output_dir = base_dir / "output"
template_dir = base_dir / "frontend"
static_dir = template_dir / "static"

app = Flask(__name__, 
            template_folder=str(template_dir), 
            static_folder=str(static_dir), 
            static_url_path='/static')

# Ensure the input/output directories exist
input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No file part", 400
    
    file = request.files['video']
    if file.filename == '':
        return "No selected file", 400
    
    # Use a secure filename to avoid directory traversal attacks
    filename = secure_filename(file.filename)
    upload_path = input_dir / filename

    try:
        # Save the uploaded file
        file.save(upload_path)

        upload_path_str = str(upload_path)

        # Transcribe the video
        transcript_video_service(upload_path_str)

        # Save the video with subtitles
        subtitle_path = output_dir / "output.srt"
        subtitle_path_str = str(subtitle_path)

        output_video_path = output_dir / "output.mp4"
        output_video_path_str = str(output_video_path)

        saver = VideoSaver(video_path=upload_path_str, subtitle_path=subtitle_path_str)
        saver.save_video_with_subtitles(str(output_video_path_str))

        # Pass the download URL to the template
        download_url = url_for('download_file', filename='output.mp4')
        return render_template('download.html', download_url=download_url)

    except Exception as e:
        return f"An error occurred: {e}", 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        output_video_path = output_dir / filename
        return send_file(output_video_path, as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    print(f"Templates Path: {template_dir}")
    print(f"Static Path: {static_dir}")
    app.run(debug=True)
