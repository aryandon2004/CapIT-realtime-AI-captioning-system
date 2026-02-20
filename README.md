# 🎤 SpeakSync — Real-Time Classroom Captioning System

SpeakSync is an AI-powered real-time speech-to-text system designed for classrooms and meetings. It generates live captions from speech with low latency and offline processing.

## Features

- Real-time caption generation
- Offline speech recognition (privacy-friendly)
- Streaming captions in browser
- Simple web interface

## Tech Stack

- Python
- Flask
- Vosk Speech Recognition
- HTML/CSS

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Download Vosk model:
   https://alphacephei.com/vosk/models

3. Extract model into the /model folder

4. Run:
   python app.py

Open http://127.0.0.1:5000
