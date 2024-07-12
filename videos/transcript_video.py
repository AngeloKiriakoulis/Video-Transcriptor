# Task 2: Create the transcript using OpenAI's Whisper pre-trained model.

import pandas as pd
from transformers import pipeline

"""pipeline(): It’s like a toolbox, handling most of the hard work. It follows specific steps to produce desired outputs for various tasks. Just select the task, and the pipeline does the rest."""

def transcript(video_file):

  transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-small")
  transcription_results = transcriber(video_file)
  transcription_text = transcription_results.get('text', "No transcription results found.")

  output = pd.DataFrame({'Video Name': [video_file],
                         "Transcript": [transcription_text]})
  
  return (video_file, transcription_text)