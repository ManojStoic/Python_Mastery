# import PyPDF2

# with open('.\docs\\twopage.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)

# with open('.\docs\\dummy.pdf','rb') as file:
#     reader = PyPDF2.PdfFileReader(file)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open('.\docs\\tiltdummy.pdf','wb') as new_file:
#         writer.write(new_file)
