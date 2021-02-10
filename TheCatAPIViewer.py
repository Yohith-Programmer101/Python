import requests
from time import sleep
from PIL import Image
import os

def check_valid_status_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_image(url):
    request = requests.get(url)
    data = check_valid_status_code(request)
    return data

image = get_image("https://api.thecatapi.com/v1/images/search")

for x in image:
    url = x['url']
    print(url)
    img = requests.get(url).content
    file = open("images/cat.jpg", "wb")
    file.write(img)
    file.close()
    im = Image.open("images/cat.jpg")
    im.show()
    sleep(10)
    im.close()
    os.unlink("images/cat.jpg")
    
