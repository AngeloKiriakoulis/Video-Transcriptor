# Task 2: Create the transcript using OpenAI's Whisper pre-trained model.
import os
import pandas as pd
import whisper
def process_transcription():
  pass

def transcript(video_file):

  model = whisper.load_model("base")
  result = model.transcribe(audio = video_file)["segments"]

  # Extracting the fields into lists
  start_times = [segment["start"] for segment in result]
  end_times = [segment["end"] for segment in result]
  texts = [segment["text"] for segment in result]

  # Creating the DataFrame
  transcript_df = pd.DataFrame({
      "start": start_times,
      "end": end_times,
      "text": texts
  })

  return (video_file, transcript_df)

# print(transcript("src/videos/1.mp4"))