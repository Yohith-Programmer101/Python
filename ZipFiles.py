import zipfile
target = "zips\\BulkFile.zip"
handle = zipfile.ZipFile(target)
listing = handle.namelist()
for i in listing:
    i = handle.getinfo(i)
    print("-"* 50)
    print("File name: ",i.filename)
    print("Before: ", i.file_size)
    print("After: ", i.compress_size)
