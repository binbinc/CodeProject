from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors

styles = getSampleStyleSheet()
doc = SimpleDocTemplate("products.pdf")
Catalog = []
header = Paragraph("Product Inventory", styles['Heading1'])
Catalog.append(header)
style = styles['Normal']
headings = ('Product Name', 'Product Description')
allproducts = [["a", "b"],
               ["aa", "bb"]]
t = Table([headings] + allproducts)
t.setStyle(TableStyle(
                [('BOX', (0,0), (1,-1), 2, colors.black),
                 ('BACKGROUND', (0, 0), (-1, 0), colors.pink)]))
Catalog.append(t) 
doc.build(Catalog)