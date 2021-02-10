import PyPDF2, os
os.chdir("C:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\documents")
pdffile = open("meetingminutes1.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdffile)
print("No.of pages: ", reader.numPages) # returns the number of pages
print("-" * 100)
page = reader.getPage(0)
print(page.extractText())
'''to extract all we can use:
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())'''
print("-" * 100)
pdffile.close()
pdf1file = open("meetingminutes1.pdf", "rb")
pdf2file = open("meetingminutes2.pdf", "rb")
reader1 = PyPDF2.PdfFileReader(pdf1file)
reader2 = PyPDF2.PdfFileReader(pdf2file)
writer = PyPDF2.PdfFileWriter()
for pagenum in range(reader1.numPages):
    page = reader1.getPage(pagenum)
    writer.addPage(page)
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
outputFile = open("combinedminutes.pdf", "wb")
writer.write(outputFile)
outputFile.close()
pdf1file.close()
pdf2file.close()
