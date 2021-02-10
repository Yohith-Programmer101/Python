import zipfile
target = "zips\\bulkFile.zip"
result = zipfile.ZipFile(target)
for i in result.namelist():
    if i.endswith(".txt"):
        result.extract(i, "zips")
# to extract all we can use result.extractall() in place of result.extract()
