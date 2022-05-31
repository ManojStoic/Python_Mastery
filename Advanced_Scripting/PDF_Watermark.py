import PyPDF2
import sys

def AddWatermark(wm_file,main_file):
    mf_obj = PyPDF2.PdfFileReader(main_file)
    wm_obj = PyPDF2.PdfFileReader(wm_file)
    writer_obj = PyPDF2.PdfFileWriter()
    wm_page = wm_obj.getPage(0)
    for page in range(0,mf_obj.getNumPages()):
        mf_page = mf_obj.getPage(page)
        mf_page.merge_page(wm_page)
        writer_obj.addPage(mf_page)
    with open(main_file,'wb') as outfile:
        writer_obj.write(outfile)

AddWatermark(sys.argv[1],sys.argv[2])