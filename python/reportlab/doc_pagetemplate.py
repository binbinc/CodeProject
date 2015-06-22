from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, PageTemplate, Image
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer

doc = BaseDocTemplate('test7.pdf',showBoundary=1)
styles=getSampleStyleSheet()
story=[]

def static_title(canvas,doc):
    canvas.saveState()
    canvas.drawImage('mj.png',doc.width-2.5*inch,doc.height, width=4*inch, preserveAspectRatio=True)
    canvas.setFont('Times-Roman',48)
    canvas.drawString(inch, doc.height - 1*inch, "TITLE")
    canvas.restoreState()
    
def static_back(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Back")
    canvas.restoreState()

def static_1col(canvas,doc):
    canvas.saveState()
    canvas.drawImage('mj.png',doc.width+0.5*inch,doc.height+0.5*inch, width=1*inch, preserveAspectRatio=True)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "One Col - Page %d" % doc.page)
    canvas.restoreState()

def static_2col(canvas,doc):
    canvas.saveState()
    canvas.drawImage('mj.png',doc.width+0.5*inch,doc.height+0.5*inch, width=1*inch, preserveAspectRatio=True)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Two Col - Page %d" % doc.page)
    canvas.restoreState()

frame_title = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 5*inch, id='normal')
frame_back = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 8*inch, id='normal')

frame_1col = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')

frame1_2col = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='col1')
frame2_2col = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6,
               doc.height, id='col2')

doc.addPageTemplates([
        PageTemplate(id='Title',frames=frame_title,onPage=static_title),  
        PageTemplate(id='Back',frames=frame_back,onPage=static_back),  
        PageTemplate(id='OneCol',frames=frame_1col,onPage=static_1col),  
        PageTemplate(id='TwoCol',frames=[frame1_2col,frame2_2col],onPage=static_2col),
                      ])


story.append(Paragraph("Title, "*100,styles['Normal']))
story.append(NextPageTemplate('OneCol'))
story.append(PageBreak())
for i in range(0,55): 
    story.append(Paragraph("lipsum()",styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(NextPageTemplate('TwoCol'))

story.append(PageBreak())
for i in range(0,55): 
    story.append(Paragraph("lipsum",styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(NextPageTemplate('OneCol'))
story.append(PageBreak())
for i in range(0,5): 
    story.append(Paragraph("lipsum",styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(Image('mj.png'))
for i in range(0,5): 
    story.append(Paragraph("lipsum",styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(NextPageTemplate('Back'))
story.append(PageBreak())
story.append(Paragraph("Back, "*100,styles['Normal']))

doc.build(story)

