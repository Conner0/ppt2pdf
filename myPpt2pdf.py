import ppt2pdf
from ppt2pdf.main import convert
for i in range(17):
    i=i+1
    a=str(i)
    p1 = "C:\dl\Lecture"+a+".pptx"
    p2 = "C:\dl\Lecture"+a+".pdf"
    convert(p1, p2)

