# -*- coding: utf-8 -*-

"""
假定你有一个很无聊的任务，需要将几十个PDF 文件合并成一个PDF 文件。每
一个文件都有一个封面作为第一页，但你不希望合并后的文件中重复出现这些封
面。即使有许多免费的程序可以合并PDF，很多也只是简单的将文件合并在一起。
让我们来写一个Python 程序，定制需要合并到PDF 中的页面。
"""
import PyPDF2, os

pdfFiles = []

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)


pdfFiles.sort(key=str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.isEncrypted)
    if pdfReader.isEncrypted == True:
        pdfReader.decrypt('rosebud')

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

os.chdir('/Users/zhuangganglong/python/getStartedWithQuickProgramming')
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()