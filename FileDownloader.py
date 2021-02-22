import urllib.request
import os
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def download_url(url, output_path):
    os.chdir(output_path)
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        urllib.request.urlretrieve(
            url, filename=url.split('/')[-1], reporthook=t.update_to)


download_url("https://file-examples-com.github.io/uploads/2017/11/file_example_MP3_5MG.mp3",
             "./downloads")
