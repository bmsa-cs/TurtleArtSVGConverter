from turtle import *  # @UnusedWildImport
import svgwrite
#define
def draw():
    fillcolor('blue')
    begin_fill()
    for i in range(20):
        d = 50 + i*i*1.5
        pencolor(0, 0.05*i, 0)
        width(i)
        forward(d)
        right(144)
    end_fill()
