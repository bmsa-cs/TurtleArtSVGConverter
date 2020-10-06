"""
All-Student Turtle Art SVG Generator
Scans the 'art' directory for all python files and 
calls the draw() function in each one so it writes to an SVG file in the 'out' folder.

"""

#imports

from turtle import Turtle
import os
import sys
import importlib

import svgwrite

from svg_turtle import SvgTurtle

def write_file(draw_func, filename, size):
    # Uses svgwrite to export the turtle drawing to the out directory.
    drawing = svgwrite.Drawing("out/"+filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()
    
#https://stackoverflow.com/questions/31661188/import-files-in-python-with-a-for-loop-and-a-list-of-names
gbl = globals()
dir_list = os.listdir("art")

for x in dir_list: # For each file in art folder...
    if x.endswith(".py"): # Only .py files!
        try:
            x = x.replace(".py", "")

            # Import file as module
            moduleToImport = 'art.'+x
            gbl[moduleToImport] = importlib.import_module(moduleToImport)

            # Use the module to call draw() and write the file.
            write_file(gbl[moduleToImport].draw, x+'.svg', size=("500px", "500px"))
            print("Wrote file", x + '.svg')
        except Error:
            print:('Error with file ', x,'.')

