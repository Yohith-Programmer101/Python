from pyzbar.pyzbar import decode
import cv2
import webbrowser
from selenium import webdriver
import os
img = cv2.imread(r"images\QRCode.png")
de = decode(img)
url = de[0][0]
print(url)
webbrowser.open(url)
