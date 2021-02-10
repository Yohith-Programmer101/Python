import re
print("To check if it is a valid email.")
text = input("Enter a text: ")
pattern = re.compile("[a-zA-Z0-9.\-_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
res = pattern.findall(text)
if res == []:
    print("Not valid.")
else:
    print(f"Valid: {', '.join(res)}")
