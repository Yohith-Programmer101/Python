import vlc
import pafy
import time
import webbrowser

# sample video link : https://www.youtube.com/watch?v=Y8Tko2YC5hA

url = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
inp = input("Open in Web browser ? (y or n): ").lower()
if inp == "y":
    print("Opening in Web browser")
    webbrowser.open(playurl)
else:
    print("Opening in gui")
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    # player.start() // resume
    # player.pause() // pause
    # player.stop() // stops/ends
