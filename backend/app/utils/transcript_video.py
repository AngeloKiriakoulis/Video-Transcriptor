from itertools import zip_longest
from pathlib import Path
import whisper
from moviepy.editor import VideoFileClip
import librosa

class Transcriptor:
  def __init__(self, model_size="base"):
    # Load the Whisper model
    self.model = whisper.load_model(model_size)

  def transcribe_to_srt(self, video_file, output_file, pivot=1):
    print(f"Processing video file: {video_file}")
    audio_path = video_file.with_suffix(".wav")

    video = VideoFileClip(str(video_file))
    video.audio.write_audiofile(str(audio_path))

    try:
      audio, sr = librosa.load(audio_path, sr=None)
      if sr != 16000:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
        sr = 16000  # Update the sample rate for clarity

      # Step 2: Transcribe the extracted audio
      result = self.model.transcribe(audio=audio, word_timestamps=True, verbose= False)
    # Initialize variables for .srt formatting
      srt_output = []
      counter = 1
    
    # Loop through the segments and generate .srt format
      for segment in result["segments"]:
        # Use zip_longest with a fillvalue of None to handle incomplete chunks
        for word_group in zip_longest(*(iter(segment["words"]),) * pivot, fillvalue=None):
          # Filter out any None values from word_group
          valid_words = [w for w in word_group if w is not None]
          
          if not valid_words:
              continue  # Skip empty word groups

          # Concatenate the words and retrieve start and end times
          start_time = valid_words[0]['start']
          end_time = valid_words[-1]['end']
          text = ''.join(w['word'] for w in valid_words).strip()

          # Format time for SRT (hours:minutes:seconds,milliseconds)
          start_time_str = self._format_time(start_time)
          end_time_str = self._format_time(end_time)

          # Create .srt entry
          srt_entry = f"{counter}\n{start_time_str} --> {end_time_str}\n{text}\n\n"
          srt_output.append(srt_entry)
          counter += 1
          print(srt_entry)
    # Write to .srt file
      with open(output_file, "w") as file:
        file.writelines(srt_output)
    except Exception as e:
      print(f"Problem at transcription to SRT: {e}")
    
  @staticmethod
  def _format_time(seconds):
    # Helper method to format time in SRT style
    milliseconds = int((seconds % 1) * 1000)
    hours, remainder = divmod(int(seconds), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"