from videos.play_video import play
from videos.transcript_video import transcript, process_transcription
import warnings
warnings.filterwarnings("ignore")

filename, tran = transcript(video_file="videos/1.mp4")
transcription = process_transcription(tran)
play(filename,tran)