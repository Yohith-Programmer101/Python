import send2trash as s2t, os
target = "C:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\demo\\"
print()
for i in os.listdir(target):
    if i.endswith(".txt"):
        print("Files deleted:")
        print(target + i)
        s2t.send2trash(target + i)

# it is used to delete files which end as .py
# we can use os.rmdir()  or os.ulink() to delete folders or files
# to delete bulk files we can use shutil.rmtree()