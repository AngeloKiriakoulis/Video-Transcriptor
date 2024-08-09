from util.play_video import play
from util.transcript_video import transcript
import warnings
warnings.filterwarnings("ignore")

filename, tran = transcript(video_file="videos/1.mp4")
play(filename,tran)