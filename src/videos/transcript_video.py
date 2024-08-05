# Task 2: Create the transcript using OpenAI's Whisper pre-trained model.
import os
import pandas as pd
import whisper
import warnings
warnings.filterwarnings("ignore")

def transcript(video_file):
  model = whisper.load_model("base")
  result = model.transcribe(audio = video_file, word_timestamps=True)

  # Extracting the fields into lists
  start_times = [word["start"] for segment in result["segments"] for word in segment["words"]]
  end_times = [word["end"] for segment in result["segments"] for word in segment["words"]]
  words = [word['word'] for segment in result["segments"] for word in segment["words"]]

  # Creating the DataFrame
  transcript_df = pd.DataFrame({
      "start": start_times,
      "end": end_times,
      "word": words
  })

  return (video_file, transcript_df)

# print(transcript("src/videos/1.mp4"))