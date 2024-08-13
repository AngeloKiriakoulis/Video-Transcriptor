import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.play_video import play
from utils.transcript_video import transcript


def process_video(video_file):
    filename, tran = transcript(video_file=video_file)
    play(filename, tran)
    return filename, tran