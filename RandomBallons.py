
from drawingpanel import *
import time
from random import choice
import random
p = DrawingPanel(400, 400, background="light gray")

def main():
    number=random.randint(1,20)
    print(number)
    for i in range(0,20):
        hex_chars=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        colorcode="#"
        randnumber=random.randint(1,2)
        colorcode=colorcode + choice(hex_chars)
        colorcode=colorcode + choice(hex_chars)
        colorcode=colorcode + choice(hex_chars)
        colorcode=colorcode + choice(hex_chars)
        colorcode=colorcode + choice(hex_chars)
        colorcode=colorcode + choice(hex_chars)
        x1=random.randint(0,400)
        x2=random.randint(0,400)
        x3=random.randint(0,400)
        number=random.randint(0,3)
        if(randnumber==1):
            ball= p.canvas.create_oval(x1,x1,x2,x2,fill=colorcode,outline="")
        else:
            ball= p.canvas.create_oval(x2,x2,x1,x1,outline=colorcode)



main()
    
