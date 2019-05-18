import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super (Window, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("CLMITS Rocks!")
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        self.home()
    
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        # btn.resize(250,100)
        # btn.resize(btn.sizeHint())
        # btn.resize(btn.minimumSizeHint())
        btn.move(125, 250)
        self.show()

    def close_application(self):
        print("Exiting Window...")
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()