from reportlab import platypus
from reportlab.lib.units import inch
 
def genList():
    return [1, 2, 3, 4, 5, 6, 7]

def genTable():
    data = []
    items = genList()  
    for i in range(0, len(items), 5):
        data.append(items[i:i+5])
    table = platypus.Table(data, 1.5*inch, 0.4*inch, [('FONT', (0,0), (-1,-1), 'Courier')])

    return table
 
doc = platypus.SimpleDocTemplate("test.pdf", topMargin=0.9*inch, bottomMargin=0.9*inch, title='DaDa Math', author='qyb')
 
elements = []
for i in range(20):
    elements.append(genTable())
    elements.append(platypus.flowables.PageBreak())
 
doc.build(elements)