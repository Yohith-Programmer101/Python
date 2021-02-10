import pyautogui as gui
print(gui.size()) # returns the size of the screen
width, height = gui.size() # unpacks the size
print("Widht: ", width) # returns the width of the sreen
print("Height: ", height) # returns the height of the screen
print(gui.position()) # returns the current position of the cursor in the screen
gui.moveRel(0,-100) # moves the cursor -100 that is 100 pixels up
gui.moveTo(1238, 31, duration = 2) # the cursor moves to that coordinate with total duration of 2 sec, we can also use this without the duration the default duraton is rapid fast
gui.moveTo(1303, 0) # movest the cursor to that coordinate
gui.click() # it will just click # in this case it will maximize the screen
gui.click(996, 261) # we can also use click directly without moving the cusor
'''
we can also use :
gui.doubleClick() # to double click the screen
gui.leftClick() # to left click the screen 
gui.rightClick() # to right click the screen 
gui.middleClick() # to middle click the screen 
'''
'''
we can use this command in the cmd by opening python in the cmd by typing python in the cmd and run this,
import pyautogui as gui
gui.displayMousePosition()
'''
# importatnt note:
# to terminate the process of the pyautogui mouse automation by just movindg the cursor to the 0, 0 coordinate of the screen that is the top most left corner of the screen
