import time
import uuid
from flask import Flask, render_template, send_file, request, redirect, url_for
from flask_cors import CORS
from pathlib import Path
from services.transcription_service import transcript_video_service
from services.video_saver_service import VideoSaver

def find_project_root(current_dir: Path, marker: str = ".git") -> Path:
    """
    Recursively finds the root directory of a project by looking for a specific marker.

    Args:
        current_dir (Path): The starting directory to search from.
        marker (str): A file or folder name that identifies the project root. Default is '.git'.

    Returns:
        Path: The project root directory if found, otherwise raises a ValueError.
    """
    for parent in current_dir.resolve().parents:
        if (parent / marker).exists():
            return parent
    raise ValueError(f"Project root containing '{marker}' not found from {current_dir}")

# Initialize Flask app
current_dir = Path.cwd()

try:
    project_root = find_project_root(current_dir)
    print(f"Project root found: {project_root}")
except ValueError as e:
    print(e)

input_dir = Path(project_root,"input")
output_dir = Path(project_root,"output")
template_dir = Path(project_root,"frontend")
static_dir = Path(project_root,"static")

app = Flask(
    __name__, 
    template_folder=str(template_dir), 
    static_folder=str(static_dir), 
)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'video' not in request.files:
        return "No file part", 400
    
    file = request.files['video']
    if file.filename == '':
        return "No selected or invalid file", 400

    try:
        input_dir.mkdir(parents=True, exist_ok=True)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        unique_id = uuid.uuid4()
        upload_file = input_dir / f"{unique_id}_{file.filename}"
        
        file.save(upload_file)
        app.logger.debug(f"File saved to {upload_file}")

        
        subtitle_path = output_dir / f"{unique_id}.srt"
        transcript_video_service(upload_file,subtitle_path)  # Convert to str if required
        output_video_path = output_dir / f"{unique_id}.mp4"

        saver = VideoSaver(video_path=upload_file, subtitle_path=subtitle_path)
        saver.save_video_with_subtitles(str(output_video_path))
        
        app.logger.debug(f"Output video path: {output_video_path}")
        
        download_url = url_for('download_file', filename=str(output_video_path))
        return render_template('download.html', download_url=download_url)
    except Exception as e:
        import traceback
        app.logger.error(f"Error during upload: {traceback.format_exc()}")
        return "An error occurred during processing.", 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        output_video_path = output_dir / filename
        return send_file(str(output_video_path), as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__ == '__main__':
    print(f"Templates Path: {template_dir}")
    print(f"Static Path: {static_dir}")
    app.run(host='0.0.0.0', port=5000, debug=True)


