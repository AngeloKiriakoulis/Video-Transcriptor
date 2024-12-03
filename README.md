# Automatic Video Transcriptor and Subtitle Generator

## Outline

- [Description](#description)
- [Features](#features)

## Description

This project automates the process of video transcription and word-level subtitle generation using OpenAI's Whisper model. It is designed to create synchronized subtitles similar to those seen in TikTok and Instagram Reels, where each word is displayed in real-time as it is spoken. The project outputs both `.srt` files and videos with embedded subtitles.

## Overview of Architecture

This diagram illustrates a typical architecture combining **Firebase Hosting**, **Cloud Run**, and a **Database** to deliver dynamic web applications:

![Screenshot (76)](https://github.com/user-attachments/assets/133beb3d-bc92-4fe2-aa25-7993d9143b10)

1. **Web Browser**: Initiates requests and displays the final webpage to the user.
2. **Firebase Hosting**: Serves static assets (HTML, CSS, JS) and acts as the frontend hosting service.
3. **Cloud Run**: Handles backend processing, including API calls and communication with the database.
4. **Database**: Stores and retrieves the data used by the application.

The overall workflow is as follows:
- The user clicks or requests a page, initiating a sequence of events.
- Firebase Hosting serves the initial HTML/JS template and may make an API call to the backend (Cloud Run).
- Cloud Run processes the request and interacts with the database to read or write data.
- The data is sent back to the frontend for rendering and is displayed to the user.

## Features

- **Automatic Transcription**: Converts spoken words in videos into text using the Whisper model.
- **Word-Level Subtitles**: Generates subtitles that appear in sync with each word spoken in the video.
- **Silence Detection**: Automatically detects and excludes long periods of silence from the subtitle file.
- **User Interface**: (Planned) A simple UI to upload videos, generate subtitles, and download the results.
- **Playback Verification**: A service to play back the video with subtitles for synchronization checking.
