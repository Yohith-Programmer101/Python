import pyautogui
import PyPDF2


pdf1 = pyautogui.prompt(text='Enter the location of the first PDF', title='PDF merger' , default='None')
pdf2 = pyautogui.prompt(text='Enter the location of the second PDF', title='PDF merger' , default='None')
pdf3 = pyautogui.prompt(text='Enter the location of the merged PDF', title='PDF merger' , default='None')
pdf1file = open(pdf1, "rb")
pdf2file = open(pdf2, "rb")
reader1 = PyPDF2.PdfFileReader(pdf1file)
reader2 = PyPDF2.PdfFileReader(pdf2file)
writer = PyPDF2.PdfFileWriter()
for pagenum in range(reader1.numPages):
    page = reader1.getPage(pagenum)
    writer.addPage(page)
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
outputFile = open(pdf3, "wb")
writer.write(outputFile)
outputFile.close()
pdf1file.close()
pdf2file.close()

