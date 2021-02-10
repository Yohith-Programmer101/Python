import pyperclip
a = "hello, world!"
pyperclip.copy(a)
print("Test copied")
print("Do you want to know whether pyperclip works properly or not")
inp = input("Either enter yes or y or no n: ").lower()
if inp == "yes" or "y":
    print("PYPERCLIP CHECK:")
    i = input("Paste your copied test here: ")
    if i == a:
        print("Works properly")
    else:
        print("Not works properly")
