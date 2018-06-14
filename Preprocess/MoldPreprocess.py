from Preprocess.convertimg import *
from PyPDF2 import PdfFileWriter, PdfFileReader
import pathlib
import os

outfolder = '..\\Data\\Pre_Product'
pdffolder = '..\\Data\\PDF_Product'
inputfolder = '..\\Data\\Product'

pathlib.Path(outfolder).mkdir(parents=True, exist_ok=True)
pathlib.Path(pdffolder).mkdir(parents=True, exist_ok=True)

for file in os.listdir(inputfolder):
    extension = file[file.find('.')+1:]
    filedir = os.path.join(inputfolder,file)

    if extension == 'pdf':
        # pdf 이미지 분할
        pdfsplit(filedir,pdffolder)

        # pdf 이미지 저장
        if pdf in os.listdir(pdffolder):
            pdf2img()
    # else :

