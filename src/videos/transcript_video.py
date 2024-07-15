# Task 2: Create the transcript using OpenAI's Whisper pre-trained model.
import pandas as pd
import whisper

def transcript(video_file):

  model = whisper.load_model("base")
  result = model.transcribe(video_file)["segments"]

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

  print(transcript_df)

transcript("src/videos/1.mp4")