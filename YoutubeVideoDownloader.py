import os
import pafy
import urllib.request
import os
from tqdm import tqdm
import math
from ConvertFileSize import convert_size

# Sample Link : https://www.youtube.com/watch?v=Y8Tko2YC5hA
link = "https://www.youtube.com/watch?v=Y8Tko2YC5hA"
yt = pafy.new(link)
print(f'''Title: {yt.title}
Image URL: {yt.thumb}
Duration: {yt.duration}
Views: {"{:,}".format(yt.viewcount)}
Ratings: {yt.rating}
Likes: {"{:,}".format(yt.likes)}
Dislikes: {"{:,}".format(yt.dislikes)}
Link: {yt.getbest().url}
File Size: {convert_size(yt.getbest().get_filesize())}
''')


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    os.chdir(output_path)
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc="Download") as t:
        urllib.request.urlretrieve(
            url, filename="YoutubeVideo.mp4", reporthook=t.update_to)


inp = input("Download the video ? (y or n): ").lower()
if inp == "y":
    download_url(yt.getbest().url, "./Downloads")
else:
    print("Thank you!")
