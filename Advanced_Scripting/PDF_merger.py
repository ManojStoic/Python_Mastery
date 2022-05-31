import PyPDF2
import sys


try:
    inputs = sys.argv[1:]
    merger = PyPDF2.PdfFileMerger()    
    for file in inputs:
        merger.append(file)
    merger.write('.\docs\Merged_file.pdf')
    # with open('.\docs\Merged_file.pdf','wb') as merged_file:
    # merger.write(merged_file)

except Exception as err:
    print(err.message)

