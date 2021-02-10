import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognising...")
        text = r.recognize_google(audio)
    except:
        print("ERROR!")
        return -1

    return str(text)

print(listen())