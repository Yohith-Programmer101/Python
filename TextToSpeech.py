import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    print("Speaking....")
    engine.say(text)
    engine.runAndWait()
    print("Spoke.")

while True:
    speak(input("Enter a text to speak: "))
