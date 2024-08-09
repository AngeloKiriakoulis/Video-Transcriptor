import sys
import os
from utils.play_video import play
from utils.transcript_video import transcript
import warnings
warnings.filterwarnings("ignore")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

filename, tran = transcript(video_file="videos/1.mp4")
play(filename,tran)