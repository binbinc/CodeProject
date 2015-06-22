from reportlab.lib import colors
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, LongTable, TableStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Spacer
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, PageTemplate, NextPageTemplate, KeepTogether, FrameBreak

styles=getSampleStyleSheet()
data = "lorem ipsum dolor sit amet consetetur sadipscing elitr sed diam nonumy eirmod tempor invidunt ut labore et".split()

doc = SimpleDocTemplate("test11.pdf", pagesize = A4, leftMargin = 0, rightMargin = 0, topMargin = 0, showBoundary=1)

Elements=[]
p1 = Paragraph("I am column 1! " * 300, styles['Normal'])
p2 = Paragraph("I am column 2! " * 800, styles['Normal'])

frame1 = Frame(1.45*cm, doc.bottomMargin + 1*cm, doc.width/2-1.45*2*cm, doc.height-7*cm, id='col1')
frame2 = Frame(doc.width/2 + 1.45*cm, doc.bottomMargin + 1*cm, doc.width/2-1.45*2*cm, doc.height-7*cm, id='col2')

doc.addPageTemplates([
    PageTemplate(id = 'TwoCol', frames = [frame1,frame2], ),
])

Elements.append(NextPageTemplate('TwoCol'))
Elements.append(KeepTogether(p1))
Elements.append(FrameBreak())   
Elements.append(KeepTogether(p2))

doc.build(Elements)