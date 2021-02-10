import os, shutil
os.chdir("c:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files")
shutil.copy("text files\\text.txt", "c:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\backups")
# to copy large amount of files we should use shutil.copytree
# we can also loacte originals\\text.txt directly without os.chdir
