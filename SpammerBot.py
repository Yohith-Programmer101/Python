import pyautogui as gui
gui.click()
for i in range(25):
    gui.typewrite("You are being spammed!")
    gui.press("enter")
