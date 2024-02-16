from pytube import Playlist

def get_playlist(playlists):
    urls = []
    for playlist in playlists:
        playlist_urls = Playlist(playlist)

        for url in playlist_urls.video_urls:
            urls.append(url)

    return urls

Playlists = ["https://www.youtube.com/playlist?list=PLpH_mDj0fStVgUZ3clTn8P83nh_yA6ZQi"]
urls = get_playlist(Playlists)
print(urls)
