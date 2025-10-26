<p align="center">
  <img src="assets/logo.png" alt="subgenX Logo" width="160"/>
</p>

<h1 align="center">subgenX</h1>

<p align="center">
  <strong>Offline Subtitle Generator for Kodi</strong><br>
  Generate subtitles for TV Shows, Movies, and Music locally — no internet required.
</p>

<p align="center">
  <img src="./resources/icon.png" />
</p>

---

## 📖 About

**subgenX** is a **Kodi addon** designed to generate subtitles **entirely offline** using local machine learning models like **OpenAI Whisper**.  
It works seamlessly with your current playback, automatically transcribing and syncing subtitles for movies, TV shows, or even music videos.

> No internet. No external APIs. Just pure local processing.

---

## ⚙️ Features

- 🎬 Generate subtitles for any media (video/audio)
- ⚡ Works fully offline — ideal for privacy and air-gapped systems
- 🧠 Powered by Whisper (OpenAI) for accurate speech recognition
- 🗂️ Auto-detects current playing file in Kodi
- 📝 Supports `.srt` subtitle output
- 🖥️ Simple Kodi UI and success notifications

---

## 🚀 Installation

### 🔹 Method 1 — Manual Install

1. Clone or download this repository:

   ```bash

   git clone https://github.com/BossySmaxx/subgenX.git [inside your kodi addon folder]
   ```

## ⚙ Dependencies

### 🔹 openai-whisper

### 🔹 [ffmpeg-essentials](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) <- (Recommended)

#### 🔹 if the above link doesn't work you can try these links below:

- https://www.gyan.dev/ffmpeg/builds
- https://www.ffmpeg.org/download.html#build-windows

## 👩‍🔧 Install Dependencies

```bash
pip install -U openai-whisper ffmpeg-python
```
