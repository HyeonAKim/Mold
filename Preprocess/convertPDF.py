from PyPDF2.PyPDF2 import PdfFileWriter, PdfFileReader


def pdfsplit():
    inputpdf = PdfFileReader(open("/Users/hyeonakim/PycharmProjects/MoldDesign/Data/rawData/testpdf.pdf", "rb"))

    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open("document-page%s.pdf" % i, "wb") as outputStream:
            output.write(outputStream)

