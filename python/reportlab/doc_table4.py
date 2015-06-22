from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table
from reportlab.lib.units import cm

width, height = A4
styles = getSampleStyleSheet()

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

descrpcion = Paragraph('long paragraph', styles["Normal"])
partida = Paragraph('1', styles["Normal"])
candidad = Paragraph('120', styles["Normal"])
precio_unitario = Paragraph('$52.00', styles["Normal"])
precio_total = Paragraph('$6240.00', styles["Normal"])

data= [[partida, candidad, descrpcion, precio_unitario, precio_total]]
table = Table(data, colWidths=[2.05 * cm, 2.7 * cm, 9.6 * cm,
                               2.65 * cm, 2.7 * cm])

c = canvas.Canvas("kk.pdf", pagesize=A4)
table.wrapOn(c, width, height)
table.drawOn(c, *coord(1.8, 9.6, cm))
c.save()