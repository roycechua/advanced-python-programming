"""This Example shows how to create an object-oriented window with MAIN"""
import sys
from PyQt4 import QtGui

class Window(QtGui.QMainWindow):
    def __init__(self):
        super (Window, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("CLIMTS Rocks!")
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        
        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+X")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)
        self.statusBar()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extractAction)
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