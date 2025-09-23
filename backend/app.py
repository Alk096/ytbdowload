from fastapi import FastAPI
import json
import yt_dlp
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

options = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=options,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.expanduser("~/Downloads")

@app.get("/")
def read_root():
    return {"message": "YouTube Downloader API is running 🚀"}

@app.get("/download/video")
async def download(url : str):
    try:
        ffmpeg_path = shutil.which("ffmpeg") is not None

        ydl_opts = {
            "format": "bestvideo+bestaudio/best" if ffmpeg_path else "best",
            "merge_output_format": "mp4" if ffmpeg_path else None,
            "outtmpl": os.path.join(BASE_DIR, "%(title)s.%(ext)s"),
            "noplaylist": True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {
            "type": "Video",
            "message": "Video Downloaded Succesfully"
        }
    except Exception as e:
        return { "Error -> ": str(e) }


@app.get('/download/playlist/')
async def download_playlist(url : str):
    try:
        ffmpeg_path = shutil.which("ffmpeg") is not None

        ydl_opts = {
            "format": "bestvideo+bestaudio/best" if ffmpeg_path else "best",
            "merge_output_format": "mp4" if ffmpeg_path else None,
            "outtmpl": os.path.join(BASE_DIR, "%(title)s.%(ext)s"),
            "noplaylist": False
        }
        with  yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {
            "type": "playlist",
            "message": "Playlist Downloaded and Merged Successfully"
        }
    except Exception as e:
        return { "Error -> ": str(e) }