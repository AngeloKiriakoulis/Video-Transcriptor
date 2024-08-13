import pandas as pd
from utils.transcript_video import transcript

result1 = transcript("videos/1.mp4")
result2 = transcript("videos/1.mp4")
tran = result1[1]

def test_result_type():
    # Test the function with a valid .mp4 file path
    assert isinstance(result1, tuple)

def test_result_len():
    # Test the function with a valid .mp4 file path
    assert len(result1) == 2  # Assuming the tuple has two elements

def test_transcript_type():
    # Test the function with a valid .mp4 file path
    assert isinstance(tran, pd.DataFrame)

def test_empty_dataframe():
    # Test the function with a video file with no transcriptable content
    assert not tran.empty

def test_dataframe_columns():
    # Test the function with a valid .mp4 file path
    expected_columns = ["start", "end", "word"]  # Adjust according to the actual columns
    assert list(tran.columns) == expected_columns

def test_dataframe_content():
    # Test the function with a valid .mp4 file path
    assert "Today" in tran["word"].values  # Example text to check for
    assert tran["start"].min() >= 0  # Ensure valid start times

def test_consistent_results():
    # Test the function multiple times with the same .mp4 file
    pd.testing.assert_frame_equal(result1[1], result2[1])
