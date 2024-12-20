from pathlib import Path
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.subtitles import SubtitlesClip
import os
class VideoSaver:
  def __init__(self, video_path, subtitle_path=None):
    self.video_path = video_path
    self.subtitle_path = subtitle_path

  def save_video_with_subtitles(self, output_path):
    # Load the video file
    video_clip = VideoFileClip(str(self.video_path))
    # If subtitle path is provided, add subtitles to the video
    if self.subtitle_path and os.path.exists(str(self.subtitle_path)):
      # Create a SubtitlesClip object from the .srt file
      generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='white')
      subtitles = SubtitlesClip(str(self.subtitle_path), generator)  
      # Overlay the subtitles on the video
      video_with_subtitles = CompositeVideoClip([video_clip, subtitles.set_pos(('center', 'center'))])
    else:
      video_with_subtitles = video_clip
    
    # Save the video with subtitles, ensuring correct audio handling
    video_with_subtitles.write_videofile(
      output_path,
      codec="libx264",
      audio_codec="aac",
      temp_audiofile="temp-audio.m4a",
      remove_temp=True,
      fps=video_clip.fps
    )