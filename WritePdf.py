from fpdf import FPDF
import PyPDF2
import os

os.chdir ("c:\\Users\\User\\Desktop\\PROGRAMS\\python\\Pycharm Project Files\\documents")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.cell(200, 10, txt="HELLO THIS IS A PDF", ln=1, align="C")
pdf.output("WriterPdf.pdf")


read = open("WriterPdf.pdf", "rb")
reader = PyPDF2.PdfFileReader(read)
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
read.close()