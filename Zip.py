import zipfile, os
os.chdir("C:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\zips\\BulkFile")
target = "text-0.txt" # it can only open files not folders
handle = zipfile.ZipFile("C:\\Users\\User\\Desktop\\hello.zip", "w")
handle.write(target, compress_type = zipfile.ZIP_DEFLATED)
handle.close()

