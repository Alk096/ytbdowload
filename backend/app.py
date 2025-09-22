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
    ffmeg_path = shutil.which("ffmpeg") is not None
    
    if ffmeg_path:
        ydl_opts = { 
            "format" :"bestvideo+bestaudio/best",
            "merge_output_format" : "mp4",
            "outtmpl" : os.path.join(BASE_DIR, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {"message": "Download and Merged Successfully"}
    else:
        ydl_opts = {
            "format" : "best",
            "outtmpl" : os.path.join(BASE_DIR, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {"message": "Downloaded Successfully without Merging"}


@app.get('/download/playlist/')
async def download_playlist(url : str):
    ffmeg_path = shutil.which("ffmpeg") is not None
    
    if ffmeg_path:
        ydl_opts = {
            "format" : "bestvideo+bestaudio/best",
            "merge_output_format" : "mp4",
            "outtmpl" : os.path.join(BASE_DIR, '%(playlist_title)s', '%(playlist_index)s-%(title)s.%(ext)s')
        }
        with  yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {"message": "Playlist Downloaded and Merged Successfully"}
    else:
        ydl_opts = {
            "format" : "best",
            "outtmpl" : os.path.join(BASE_DIR, '%(playlist_title)s', '%(playlist_index)s-%(title)s.%(ext)s')
        }
        with  yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
        return {"message": "Playlist Downloaded Successfully without Merging"}