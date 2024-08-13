# Automatic Video Transcriptor and Subtitle Generator

## Outline

- [Description](#description)
- [Features](#features)

## Description

This project automates the process of video transcription and word-level subtitle generation using OpenAI's Whisper model. It is designed to create synchronized subtitles similar to those seen in TikTok and Instagram Reels, where each word is displayed in real-time as it is spoken. The project outputs both `.srt` files and videos with embedded subtitles.

## Features

- **Automatic Transcription**: Converts spoken words in videos into text using the Whisper model.
- **Word-Level Subtitles**: Generates subtitles that appear in sync with each word spoken in the video.
- **Silence Detection**: Automatically detects and excludes long periods of silence from the subtitle file.
- **User Interface**: (Planned) A simple UI to upload videos, generate subtitles, and download the results.
- **Playback Verification**: A service to play back the video with subtitles for synchronization checking.
