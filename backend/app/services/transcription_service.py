import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.transcript_video import Transcriptor

def transcript_video_service(video_file):
    transcriptor = Transcriptor(model_size="base")
    transcriptor.transcribe_to_srt(video_file, "output/output.srt")

if __name__=="__main__":
    transcript_video_service("videos/input.mp4")