import os
os.chdir("C:\\Users\\User\\Desktop")
os.mkdir("BulkFile")
os.chdir("C:\\Users\\User\\Desktop\\BulkFile")
for x in range(100 + 1):
    file = open(f"text-{x}.txt", "w")
    for i in range(100 +1):
        file.write("hello, world!\n")
    file.close()
