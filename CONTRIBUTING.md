# Contributing to the Project

## Introduction

Thank you for your interest in contributing to my project! This project aims to automate video transcription and word-level subtitle generation (like in TikTok, IG Reels) using OpenAI's Whisper model. Below, you’ll find a guide to understanding the main components of the code and how you can contribute effectively.

## Main Modules

### transcribe_to_srt (Class: Transcriptor)

- **Function**: Transcribes the video using the Whisper model and generates a .srt file with word-level timestamps.
- **Current Input**: Video file path (local files).
- **Current Output**: .srt file with word-level timestamps.
- **Refactor**: *Improved Handling of Word Groups.* We now handle incomplete word groups using zip_longest, ensuring no word segments are lost, even if they don’t perfectly fit the pivot.
- **TODO**:
  - Investigate the possibility of adding more transcription models for better accuracy and language support.
  - Extend support for additional subtitle formats like vtt.

### play_video

- **Function**: A service to play the video and check the synchronization with the `.srt` file.
- **Input**: Video file and `.srt` file.
- **Output**: Playback of the video with subtitles for verification.

## Logic for Handling Silence

- **TODO:**
  - **Silence Detection**: Probably will check if the ending point of the last word is >=1sec apart of the starting point of the next word.
  - **Exclusion Approach**: When the `.srt` file is created, we will exclude these in-between time sections.
- **SOLUTION:**
  - Made with srt files exactly on the timestamps

## Input and Output Formats

- **Input**: Video/Audio uploaded by the user in the UI of the page.
- **Output**: New Video/Audio that contains the word-level subtitles.

## User Interface (UI)

- **Goal**: To provide a simple and intuitive interface that allows users to upload videos, process them, and download the resulting video with word-level subtitles.
- **TODO**:
  - Design and implement a UI that allows users to upload video/audio files.
  - Integrate the UI with the backend to trigger the transcription and subtitle generation process.
  - Display the processed video with synchronized subtitles for user verification.
  - Provide options for users to download the video with embedded subtitles or the `.srt` file separately.

## How to Contribute

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Write tests for your changes.
- Submit a pull request with a detailed explanation of your changes.
