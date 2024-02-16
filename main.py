import yt_dlp
from download import get_playlist


ydl_opts = {}

Playlists = ["https://www.youtube.com/playlist?list=PLpH_mDj0fStVgUZ3clTn8P83nh_yA6ZQi"]
urls = get_playlist(Playlists)
print(urls)

for url in urls:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])

    print("Downloaded" + info['title'])

print("Downloaded all videos")
