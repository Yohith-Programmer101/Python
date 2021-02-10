import pyqrcode
import png
from pyqrcode import QRCode
import os
os.chdir("images")
qrstring = "http://communication-bot.rf.gd"
url = pyqrcode.create(qrstring)
url.png("QRCode.png", scale = 8)