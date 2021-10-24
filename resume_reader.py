#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:01:29 2021

@author: christinayu
"""


import jieba
import glob
import random
import pdfminer
import sys

from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

    
def get_content(content_path):
    with open(content_path,'r', encoding='gbk',errors ='ignore') as f:
          content = ''
          for i in f:
             i = i.strip()
             content += i
    return content


def get_TF(k, words):
        tf_dic = {}
        for i in words:
            tf_dic[i] = tf_dic.get(i, 0) + 1
        return sorted(tf_dic.items(), key =lambda x:x[1], reverse=True)[:k]
  

def stop_words(path):
    with open(path, encoding='UTF-8') as f:
        return [l.strip() for l in f]


def pdf_to_txt(file):
    import sys, getopt
    from io import StringIO
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    import os


    def convert(fname, pages = None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)
            
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
        
        infile = file(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            int .process_page(page)
          
        infile.close()
        text = output.getvalue()
        output.close
        return text
    
    
if __name__ == '__main__':
    files = glob.glob("/Users/christinayu/Desktop/ListSpam/ListSpam-HackDuke-2021/*.txt")
    data = files.read()
    corpus = [get_content(x) for x in files]
    sample_inx = random.randint(0, len(corpus))
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words("stop_words.utf8")]
    print("You may have skills like: " + str(get_TF(10, split_words)))
    

       
    #     fp = file(data, 'rb')
    #     rsrcmgr = PDFResourceManager()
    #     retstr = io.StringI0()
    #     codec = 'utf-8'
        
    #     laparams = LAParams()
        
    #     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams = laparams)
        
    #     interpreter = PDFPageInterpreter(rsrcmgr, device)
        
    #     for page in PDFPage.get_pages(fp):
    #         interpreter.process_page(page)
    #         data = retstr.getvalue()
            
    #     print(data)
        
    # if __name__ == '__main__':
    #     pdfparser(sys.argv[1])
        
        
        
# class CsvConverter(TextConverter):
#     def __init__(self, *args, **kwargs):
#         TextConverter.__init__(self, *args, **kwargs)
        
#     def end_page(self, i):
#         from collections import defaultdict
#         lines = defaultdict(lambda : {})
#         for child in self.cur_items.objs:
#             if isinstance(child, LTTextItem):
#                 (_,_,x,y) = child.bbox
#                 line = lines[int(-y)]
#                 line[x] = child.text.encode(self.codec)
                
#         for y in sorted(lines.keys()):
#             line=lines[y]
#             self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
#             self.outfp.write("\n")        
        
        
        
        
        
    # class CsvConverter(TextConverter):
    #     def __init__(self, *args, **kwargs):
    #         TextConverter.__init__(self, *args, **kwargs)
        
    #     def end_page(self, i):
    #         from collections import defaultdict
    #         lines = defaultdict(lambda : {})
    #         for child in self.cur_items._objs:
    #             if isinstance(child, LTTextItem):
    #                 (_,_,x,y) = child.bbox
    #                 line = lines[int(-y)]
    #                 line[x] = child._text.encode(self.codec)
                    
    #         for y in sorted(lines.keys()):
    #             line = lines[y]
    #             self.outfp.write(";".join(line[x] for x in sorted(line.keys())))
    #             self.outfp.write("\n")
    #     rsrc = PDFResourceManager()
    #     outfp = StringI0()
    #     device = CsvConverter(rsrc, outfp, codec = "utf-8", laparams = LAParams())
        
    #     doc = PDFDocument()
    #     fp = open(filename, 'rb')
    #     parser = PDFParser(fp)
    #     parser.set_document(doc)
    #     doc.set_parser(parser)
    #     doc.initialize('')
        
    #     interpreter = PDFPageInterpreter(rsrc, device)
        
    #     for i, page in enumerate(doc.get_pages()):
    #         outfp.write("START PAGE %d\n" % i)
    #         if page is not None:
    #             interpreter.process_page(page)
    #         outfp.write("END PAGE %d\n" % i)
        
    #     device.close()
    #     fp.close()
        
        
            
     