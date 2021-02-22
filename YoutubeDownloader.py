import os
from pytube import YouTube

# Sample Link : https://www.youtube.com/watch?v=HnXmI2UVZlU
link = input("Enter any youtube video link: ")
yt = YouTube(link)
print(f'''Title: {yt.title}
Image URL: {yt.thumbnail_url}
Duration: {yt.length} seconds that is {yt.length/60} minutes
Views: {"{:,}".format(yt.views)}
Ratings: {yt.rating}
Description:
{yt.description}
''')
confirm = input("Do you want to download the video (y or n): ").lower()
if confirm == "y":
    loc = input("Enter the location of the folder (relative location): ")
    try:
        resolution = int(
            input("Enter the resolution without any characters like 'p' Example: 240 : "))
    except:
        resolution = int(
            input("Enter the resolution without any characters like 'p' Example: 240 : "))
    print("Started Downloading!")
    yt.streams.filter(res=str(resolution)+"p").first().download(loc)
    print("Finished Downloading!")
else:
    print("Thank you for visiting!")

'''
video = yt.streams.filter(res="240p").first()
print(video)
video.download()
yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
    'resolution').desc()
'''
