# open file: documents/locate.html and run this program
import pyautogui as gui
gui.screenshot(r"C:\Users\User\Desktop\PROGRAMS\python\Python Files\images\screenshot.png") # it takes screen shot of the screen
# # print(gui.locateOnScreen(r"C:\Users\User\Desktop\PROGRAMS\python\Pycharm Project Files\images\scrennshot.png")) # it locates the picture on the screen that is finds the picture # the parameters are: x, y, width, height # x, y are the coordinates and width, height arte the widht and height of the located picture
print(gui.locateOnScreen(r"C:\Users\User\Desktop\PROGRAMS\python\Python Files\images\locate.png")) # locates the pic in the screen # output : x, y, width, height
print(gui.locateCenterOnScreen(r"C:\Users\User\Desktop\PROGRAMS\python\Python Files\images\locate.png"))# locates the pic in the screen # ouput : x, y
gui.moveTo(gui.locateCenterOnScreen(r"C:\Users\User\Desktop\PROGRAMS\python\Python Files\images\locate.png")) # your cursor will locate the button
gui.click()# and clicks the button
