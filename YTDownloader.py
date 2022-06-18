
import pytube
from pytube import YouTube
from pytube.cli import on_progress
from pathlib import Path
downloads_path = str(Path.home() / "Downloads")
link = input('Enter Youtube Video URL: ')
yt = YouTube(link,on_progress_callback=on_progress,use_oauth=True, allow_oauth_cache=True)
video = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(downloads_path)

