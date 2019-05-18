"""This Example shows how to create a simple window using PyQt4"""

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget() 
window.setGeometry(50,50,500,500) # .setGeometry(x-coordinate,y-coordinate,Length,Width)
window.setWindowTitle("CLMITS Rocks!") # Title of the window
window.show() # Display the window

sys.exit(app.exec_()) # provides a safe exit (closes background processes)
