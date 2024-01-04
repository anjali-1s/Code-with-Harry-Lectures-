'''Write a program to manipulate pdf files using
pyPDF. Your programs should be able to merge 
multiple pdf files into a single pdf.You are 
welcome to add more.

pypdf is a free and open-source pure-python pdf
library capable of splitting, merging,cropping,
and transforming the pages of PDF files.
it can also add custom data,viewing options,
and passwords to PDF files.pypdf can retrieve 
text and metadata from PDFs as well.'''

from PyPDF import PdfWriter
# import os
merger = pdfwriter()
files = [file for file in 
os.listdir() if
file.endswith(".pdf")]

for pdf in files:
     merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()