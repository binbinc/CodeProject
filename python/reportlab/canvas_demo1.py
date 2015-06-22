from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import yellow, red, black,white

c = canvas.Canvas("hello.pdf")

u = inch/10.0
c.setStrokeColor(black)
c.setLineWidth(4)
# draw erasor
c.setFillColor(red)
c.circle(30*u, 5*u, 5*u, stroke=1, fill=1)
# draw all else but the tip (mainly rectangles with different fills)
c.setFillColor(yellow)
c.rect(10*u,0,20*u,10*u, stroke=1, fill=1)
c.setFillColor(black)
c.rect(23*u,0,8*u,10*u,fill=1)
c.roundRect(14*u, 3.5*u, 8*u, 3*u, 1.5*u, stroke=1, fill=1)
c.setFillColor(white)
c.rect(25*u,u,1.2*u,8*u, fill=1,stroke=0)
c.rect(27.5*u,u,1.2*u,8*u, fill=1, stroke=0)
c.setFont("Times-Roman", 3*u)
c.setDash([10,5,16,10],0)
c.line(11*u,2.5*u,22*u,2.5*u)
c.showPage()
c.save()
