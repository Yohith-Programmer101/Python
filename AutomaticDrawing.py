# at first open paint in your pc and select any type of brush you want and place it in the screen
import pyautogui as gui
gui.click() # click the put paint window to focus that
distance = 200
while distance > 0 :
    print(distance, 0)
    gui.dragRel(distance, 0 , duration = 0.1) # move right
    distance = distance - 25
    print(distance, 0)
    gui.dragRel(0, distance, duration=0.1)  # move down
    distance = distance - 25
    print(distance, 0)
    gui.dragRel(-distance, 0, duration=0.1)  # move left
    distance = distance - 25
    print(distance, 0)
    gui.dragRel( 0, -distance, duration=0.1)  # move up
