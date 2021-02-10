# copy any location in the clip board to search it in the google maps
import webbrowser, pyperclip
address = pyperclip.paste
webbrowser.open("https://www.google.com/maps/place/", address)
