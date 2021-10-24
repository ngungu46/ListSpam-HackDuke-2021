from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextLineHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def parsePDFtoTXT(filename):
    fp = open(filename, 'rb') #open as binary form
    parser = PDFParser(fp) #new PDFParser
    doc = PDFDocument()
    parser.set_document(doc) #pdf to PDFParser
    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager() #resource manager
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if(isinstance(x, LTTextLineHorizontal)):
                    text = x.get_text()
                    print(text)
                    with open('text.txt','a') as f:
                        f.write(text)
    fp.close()

if __name__ == '__main__':
    parsePDFtoTXT('test.pdf')