import os
target = "C:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files"
for root, dirname, files in os.walk(target):
    for x in files:
        if x.endswith(".zip"):
            print(root + "\\" + x)
# os.walk() is used to list all the directories and sub-directories that everything in that folder
