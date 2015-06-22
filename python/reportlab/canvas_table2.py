from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

# bodytext  style used for wrapping  data on flowables 
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
#used alignment if required
styleN.alignment = TA_LEFT

styleBH = styles["Normal"]
styleBH.alignment = TA_CENTER


sdName = Paragraph('''<b>LTE-IMSI based Attach</b>''', styleBH)
moduleA = Paragraph('''<b>RAN</b>''',  styleBH)
moduleB = Paragraph('''<b>CN</b>''', styleBH)

componentA = Paragraph('''<b>UE</b>''',  styleBH)
componentB = Paragraph('''<b>eNB</b>''', styleBH)
componentC = Paragraph('''<b>MME</b>''', styleBH)

produceBy = Paragraph('''<b>ZTE LTE Product</b>''', styleBH)
produceTime = Paragraph('''<b>2015.04.12</b>''', styleBH)


descrpcion = Paragraph('long long long long long long long long long long long long long long long long long long long long line ', styleN)
partida = Paragraph('1', styleN)


data= [[sdName],
       [moduleA, moduleB, '', produceBy],
       [componentA, componentB, componentC, produceTime]]

table = Table(data)

table.setStyle(TableStyle([
                       ('BOX', (0,0), (-1,2), 0.25, colors.black),
                       ('ALIGNMENT', (0,0), (-1,2), 'CENTER'),
                       ('GRID', (0,1), (-1,-1), 0.25, colors.black),
                       ]))

c = canvas.Canvas("a.pdf", pagesize=A4)
table.wrapOn(c, 50, 50)
table.drawOn(c, 100,600)
c.save()