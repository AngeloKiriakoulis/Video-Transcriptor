import os
import pytest
from app.utils.transcript_video import Transcriptor

@pytest.fixture
def transcriptor():
    return Transcriptor(model_size="base")  # Using a smaller model for testing

def test_format_time(transcriptor):
    # Test cases: (input seconds, expected formatted time)
    test_cases = [
        (0, "00:00:00,000"),
        (1.5, "00:00:01,500"),
        (65.789, "00:01:05,789"),
        (3661.123, "01:01:01,123")
    ]
    
    for seconds, expected in test_cases:
        assert transcriptor._format_time(seconds) == expected

def test_transcribe_to_srt(tmpdir, transcriptor):
    test_video_path = "videos/input.mp4"
    test_output_path = "output/output.mp4"
    # Run the transcription method
    transcriptor.transcribe_to_srt(test_video_path, test_output_path)

    # Check if the output file was created
    assert os.path.exists(test_output_path)

    # Check the contents of the SRT file
    with open(test_output_path, "r") as f:
        lines = f.readlines()
        assert len(lines) > 0  # Ensure that some content was written

    # Additional assertions can be added based on expected format/content

