import os
import pytest
from app.services.video_saver_service import VideoSaver

@pytest.fixture
def video_saver():
  video_path = "videos/input.mp4"
  subtitle_path = "output/output.srt"
  return VideoSaver(video_path, subtitle_path)

def test_save_video_with_subtitles(video_saver, tmpdir):
  # Path for the output video
  output_path = os.path.join(tmpdir, "output.mp4")

  # Run the save function
  video_saver.save_video_with_subtitles(output_path)

  # Check if the output file was created
  assert os.path.exists(output_path)
