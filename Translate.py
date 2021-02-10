from googletrans import Translator
text = input("Enter text in other language to convert it into english: ")
translator = Translator()
dt = translator.detect(text)
print(dt)
translated = translator.translate(text)
print(translated)
print(translated.text)