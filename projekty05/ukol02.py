from turtle import forward,left,right,penup, pendown,exitonclick
from math import sqrt

stranadomku = int(input("Zadej stranu domecku: "))

def domecek(stranadomku):
    #telo
    for a in range(4):
        forward(stranadomku)
        right(90)

    #strecha
    right(-45)
    forward(sqrt(2)*stranadomku/2)
    right(90)
    forward(sqrt(2)*stranadomku/2)

    #vypln
    right(90)
    forward(sqrt(2)*stranadomku)

    penup()
    left(-135)
    forward(stranadomku)
    pendown()

    left(-135)
    forward(sqrt(2)*stranadomku)


domecek(stranadomku)

exitonclick()
