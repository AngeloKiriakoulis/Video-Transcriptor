import pandas as pd
import whisper
import warnings

warnings.filterwarnings("ignore")

class Transcriptor:
  def __init__(self, model_size="base"):
    # Load the Whisper model
    self.model = whisper.load_model(model_size)
  
  def transcribe_to_df(self, video_file):
    # Transcribe the audio and get word timestamps
    result = self.model.transcribe(audio=video_file, word_timestamps=True)

    # Extracting the fields into lists
    start_times = [word["start"] for segment in result["segments"] for word in segment["words"]]
    end_times = [word["end"] for segment in result["segments"] for word in segment["words"]]
    words = [word['word'].replace(" ", "") for segment in result["segments"] for word in segment["words"]]

    # Creating the DataFrame
    transcript_df = pd.DataFrame({
      "start": start_times,
      "end": end_times,
      "word": words
    })

    return transcript_df

  def transcribe_to_srt(self, video_file, output_file):
    # Transcribe the audio and get word timestamps
    result = self.model.transcribe(audio=video_file, word_timestamps=True)

    # Initialize variables for .srt formatting
    srt_output = []
    counter = 1
    
    # Loop through the segments and generate .srt format
    for segment in result["segments"]:
      for word in segment["words"]:
        start_time = word['start']
        end_time = word['end']
        text = word['word'].strip()

        # Format time for SRT (hours:minutes:seconds,milliseconds)
        start_time_str = self._format_time(start_time)
        end_time_str = self._format_time(end_time)

        # Create .srt entry
        srt_entry = f"{counter}\n{start_time_str} --> {end_time_str}\n{text}\n\n"
        srt_output.append(srt_entry)
        counter += 1

    # Write to .srt file
    with open(output_file, "w") as file:
      file.writelines(srt_output)
  
  def _format_time(self, seconds):
    # Helper method to format time in SRT style
    milliseconds = int((seconds % 1) * 1000)
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
