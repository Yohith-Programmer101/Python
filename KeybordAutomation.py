# at first we should open a text file or any other text editors
import pyautogui as gui
gui.click();gui.typewrite("Hello, world!\n") # the semi colon is used to seperate the commands in the interactive python shell but we can use as it is in pycharm
gui.typewrite("hello, i am an automated keyboard program\n", interval=0.2) # interval makes interval between every letter
# we can use gui.KEYBOARD_KEYS to return the avilable buttons in the keyboard in a list
gui.typewrite("For Trail: ", interval=0.2)
gui.typewrite(["a", "b", "left", "left", "X", "y"], interval=0.2)
# for using a only one command or button in keyboard
gui.press("f1") # presses only one key at a time
gui.hotkey("ctrl", "s") # presses in combination of entered key
