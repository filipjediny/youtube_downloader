from lib.pytube import YouTube, 
from lib.pytube import Playlist
import re

def gen_filename(obj):
    title = re.sub(r'\([^)]*\)', '', obj.title)
    if "-" in title:
        return title+".mp4"
    if "-" in obj.author:
        return obj.author.split("-")[0]+" - "+title+".mp4"
    if "-" not in obj.author:
        return obj.author+" - "+title+".mp4"
    else:
        return title+".mp4"

while(True):
    src = input("url: ")
    if "list" in src:
        yt = Playlist(src)
        print("Downloading playlist: "+yt.title)
        for video in yt.videos:
            video.streams.get_audio_only().download("pytube_downloads\\"+yt.title,gen_filename(video))
        print("Done. Ctrl+C to close the console or enter another url.")
    else:
        yt = YouTube(src)
        print("Downloading video: "+yt.title)
        yt.streams.get_audio_only().download("pytube_downloads",gen_filename(yt))
        print("Done. Ctrl+C to close the console or enter another url.")
