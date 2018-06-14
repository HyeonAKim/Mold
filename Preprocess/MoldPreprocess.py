from Preprocess.convertimg import *
from PyPDF2 import PdfFileWriter, PdfFileReader
import pathlib
import os
import shutil

inputfolder = '..\\Data\\Product'
outfolder = '..\\Data\\Pre_Product'
pdffolder = '..\\Data\\PDF_Product'
otherfolder = '..\\Data\\Other_Product'

pathlib.Path(outfolder).mkdir(parents=True, exist_ok=True)
pathlib.Path(pdffolder).mkdir(parents=True, exist_ok=True)
pathlib.Path(otherfolder).mkdir(parents=True, exist_ok=True)
#
# #pdf 이미지분할  및 이미지파일 분할
# for file in os.listdir(inputfolder):
#     extension = file[file.find('.')+1:]
#     filedir = os.path.join(inputfolder,file)
#
#     if extension == 'pdf':
#         # pdf 이미지 분할
#         pdfsplit(filedir,pdffolder)
#     else :
#         shutil.copy(filedir,otherfolder)
#
# # pdf 이미지 변환
# for pdffile in os.listdir(pdffolder):
#     pdfdir = os.path.join(pdffolder,pdffile)
#     pdf2img(pdfdir,outfolder,'jpeg')

# other 이미지 확장자 변환
for otherfile in os.listdir(otherfolder):
    otherdir = os.path.join(otherfolder,otherfile)
    chageextension(otherdir,outfolder,'png')