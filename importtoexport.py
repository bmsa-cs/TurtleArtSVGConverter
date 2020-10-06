# All-Student Turtle Art SVG Generator
# Scans the directory for all python files and calls the draw() function in each one so it writes to an SVG file.
# imports

import turtle
import svgwrite
import os
import sys
import importlib

#gathering the files
def write_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func(draw)
    drawing.save()
    
dir_list = os.listdir()
for x in dir_list:
    try:
        open(x)
        write_file(file.draw, 'StudentTurtle.svg', size=("500px", "500px"))
    except:
        print:('Error with file ', x,'.')




#write file defined
# write_file(file.draw, 'StudentTurtle.svg', size=("500px", "500px"))

