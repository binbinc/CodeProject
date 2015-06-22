from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas


def lipsum():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ultrices ligula et libero tempus, ac pretium velit ultricies. Pellentesque sit amet vestibulum quam. Maecenas turpis ante, feugiat eu ultricies feugiat, ultricies ac elit. Praesent eleifend, nibh eu tempor consequat, nisi nunc hendrerit mi, at rhoncus massa sem quis nulla. Nunc ullamcorper mi a risus pretium, ac faucibus massa vehicula. Vestibulum venenatis aliquam felis eget hendrerit. Nulla porta massa placerat velit ultrices dictum. Curabitur mattis, lacus in convallis porta, ligula enim dignissim est, vel aliquam elit metus nec dolor. Vestibulum lacinia ac magna adipiscing iaculis. Suspendisse potenti. Nunc adipiscing magna id suscipit viverra. Sed tristique tortor ac erat mattis aliquam. Etiam nunc libero, iaculis non lectus quis, tincidunt adipiscing lacus. Aliquam in auctor dui."
#lipsum()

pdfReportPages = "test-a.pdf"
doc = SimpleDocTemplate(pdfReportPages, pagesize=A4)

# container for the "Flowable" objects
elements = []
styles=getSampleStyleSheet()
styleN = styles["Normal"]

# Make heading for each column
column1Heading = Paragraph("<para align=center>COLUMN ONE HEADING</para>",styles['Normal'])
column2Heading = Paragraph("<para align=center>COLUMN TWO HEADING</para>",styles['Normal'])
row_array = [column1Heading,column2Heading]
tableHeading = [row_array]
tH = Table(tableHeading, [6 * cm, 6 * cm])            # These are the column widths for the headings on the table
tH.hAlign = 'LEFT'
tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                       ('VALIGN',(0,0),(-1,-1),'TOP'),
                       ('BOX',(0,0),(-1,-1),1,colors.black),
                       ('BOX',(0,0),(0,-1),1,colors.black)])
tblStyle.add('BACKGROUND',(0,0),(-1,-1),colors.lightblue)
tH.setStyle(tblStyle)
elements.append(tH)

# Assemble rows of data for each column
for i in range(1,100):
    column1Data = Paragraph("<para align=center> Row  Column 1 Data  </para>", styles['Normal'])
    column2Data = Paragraph("<para align=center> Row  Column 2 Data  </para>", styleN)
    row_array = [column1Data,column2Data]
    tableRow = [row_array]
    tR=Table(tableRow, [6 * cm, 6 * cm])   
    tR.hAlign = 'LEFT'
    tR.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.white),
                            ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                            ('VALIGN',(0,0),(-1,-1),'TOP'),
                            ('BOX',(0,0),(-1,-1),1,colors.black),
                            ('BOX',(0,0),(0,-1),1,colors.black)]))
    elements.append(tR)
    del tR

elements.append(Spacer(1, 0.3 * cm))

doc.build(elements)