import os
import sys
import yt_dlp
import subprocess

video_url =  sys.argv[1]

options = {
    'format': 'bestaudio/best',
    'outtmpl': 'audios/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(options) as ydl:
    info = ydl.extract_info(video_url, download=False)
    audio_filename = ydl.prepare_filename(info)
    ydl.download([video_url])

# Convert the downloaded audio from .webm to .mp3 format using ffmpeg
mp3_filename = os.path.splitext(audio_filename)[0] + '.mp3'
subprocess.run(['ffmpeg', '-i', audio_filename, mp3_filename])

os.remove(audio_filename)

print("Audio downloaded successfully.")