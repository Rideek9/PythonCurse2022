import math

def squer():
    a = float(input('Podaj bok kwadratu:\n--> '))
    sqr = a**2
    return sqr

def rectangle():
    a = float(input('Podaj dłuższy bok prostokąta:\n--> '))
    b = float(input('Podaj krótszy bok prostokąta:\n--> '))
    rect = a*b
    return rect

def triangle():
    a = float(input('Podaj długość podstawy trójkąta:\n--> '))
    h = float(input('Podaj wysokość trójkąta:\n--> '))
    tria = (a*h)/2
    return tria

def circle():
    R = float(input('Podaj średnicę okręgu:\n--> '))
    circ = math.pi*(R/2)**2
    return circ

