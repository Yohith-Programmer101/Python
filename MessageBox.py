from pyautogui import *
print(alert(text="alert", title="messagebox", button="ok")) # creates a tkinter window with alert message box # button accepts only one string
print(confirm(text="confirm", title="messagebox", buttons=["ok", "save", "cancel"]))# creates a tkinter window with confirm message box # buttons accepts a list of strings
print(prompt(text="prompt" ,title="messagebox" , default='')) #  creates a tkinter window with prompt message  # Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or none if Cancel was clicked
print(password(text="password", title="messagebox", default="", mask="*"))