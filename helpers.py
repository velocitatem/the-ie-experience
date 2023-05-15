import sys
from PyQt5 import QtWidgets

def items_to(list, prop, value):
    # each object is a dict
    return [item for item in list if item[prop] == value]

def sdts(width, height): #scale_dimensions_to_screen
    # side_to_scale is a size of one side of a window (assuming 1920x1080)
    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    dimensions = (sizeObject.width(), sizeObject.height())
    # need to scale the side to have the appropriate ratio to the screen
    return (int(width * dimensions[0] / 1920), int(height * dimensions[1] / 1080))
