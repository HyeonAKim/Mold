from PyPDF2 import PdfFileWriter, PdfFileReader
from PIL import Image,ImageColor
from wand.image import Image
import cv2
import shutil
import os
# pdf 페이지 분할 함수
def pdfsplit(inputfile, outfile):
    inputpdf = PdfFileReader(open(inputfile, "rb"))
    filename = os.path.splitext(os.path.basename(inputfile))[0]
    outputdir = os.path.join(outfile,filename)
    if inputpdf.numPages > 1 :
        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open("%s-page%s.pdf" % (outputdir,i), "wb") as outputStream:

                output.write(outputStream)
                # print(outputStream)
    else :
        # 1장인 파일은 복사
        shutil.copy(inputfile, outfile)

# pdf 이미지 변환 함수
def pdf2img(inputfile, outfile) :
    with Image(filename=inputfile) as img:
        img.save(filename=outfile)

# 이미지 크기 변환
def resizeimg(inputfile, outfile,mode):
    #mode lower :1/4 사이즈
    #mode higher : 4배 사이즈

    img = cv2.imread(inputfile)
    if mode == 'lower' :
        resizeimage = cv2.pyrDown(img) # 원본 이미지의 1/4 사이즈 # 2000
    elif mode =='higer' :
        resizeimage = cv2.pyrUp(img) #원본 이미지의 4배 사이즈
    else :
        print("mode is lower or higher")

    print(resizeimage.shape[:2])
    cv2.imshow('resize', resizeimage)
    cv2.imwrite(outfile, resizeimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#