import os
from pathlib import Path
import sys
import cv2
import numpy as np
import os


from utils.transcript_video import Transcriptor

def transcript_video_service(video_file,output_dir): 
    transcriptor = Transcriptor(model_size="tiny")
    transcriptor.transcribe_to_srt(video_file, output_dir,3)
