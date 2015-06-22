from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, NextPageTemplate, PageBreak, FrameBreak, PageTemplate, Image, Spacer
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4, A5, landscape, portrait
from reportlab.lib.styles import getSampleStyleSheet

doc = BaseDocTemplate('test8.pdf',showBoundary=1, pagesize=landscape(A4))
styles=getSampleStyleSheet()
story=[]


def lipsum():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ultrices ligula et libero tempus, ac pretium velit ultricies. Pellentesque sit amet vestibulum quam. Maecenas turpis ante, feugiat eu ultricies feugiat, ultricies ac elit. Praesent eleifend, nibh eu tempor consequat, nisi nunc hendrerit mi, at rhoncus massa sem quis nulla. Nunc ullamcorper mi a risus pretium, ac faucibus massa vehicula. Vestibulum venenatis aliquam felis eget hendrerit. Nulla porta massa placerat velit ultrices dictum. Curabitur mattis, lacus in convallis porta, ligula enim dignissim est, vel aliquam elit metus nec dolor. Vestibulum lacinia ac magna adipiscing iaculis. Suspendisse potenti. Nunc adipiscing magna id suscipit viverra. Sed tristique tortor ac erat mattis aliquam. Etiam nunc libero, iaculis non lectus quis, tincidunt adipiscing lacus. Aliquam in auctor dui."
#lipsum()

def static_title(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',48)
    canvas.drawString(inch, doc.height - 1*inch, "TITLE")
    canvas.restoreState()
    
def static_page(canvas,doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page - Page %d" % doc.page)
    canvas.restoreState()

frame_title = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height - 5*inch, id='normal')

frame1_page = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='left')
frame2_page = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6, doc.height, id='right')

doc.addPageTemplates([
        PageTemplate(id='Title',frames=frame_title,onPage=static_title),  
        PageTemplate(id='Page',frames=[frame1_page, frame2_page],onPage=static_page),  
                      ])


story.append(Paragraph("Title, "*100,styles['Normal']))
story.append(NextPageTemplate('Page'))
story.append(PageBreak())
#story.append(Image('mj.png', width=doc.width/10))
story.append(FrameBreak())
for i in range(0,2): 
    story.append(Paragraph(lipsum(),styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(PageBreak())
for i in range(0,2): 
    story.append(Paragraph(lipsum(),styles['Normal']))
    story.append(Spacer(1,0.2*inch))
story.append(FrameBreak())
#story.append(Image('mj.png'))

doc.build(story)
