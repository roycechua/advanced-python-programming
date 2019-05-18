"""This Example shows how to create an object-oriented window with MAIN"""
import sys
from PyQt4 import QtGui, QtCore

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
        btn.resize(btn.minimumSizeHint())
        btn.move(125, 250)

        extractAction = QtGui.QAction(QtGui.QIcon('images/home.png'), "Home", self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar  = self.addToolBar("Home")
        self.toolBar.addAction(extractAction)

        checkBox = QtGui.QCheckBox("Enlarge Window", self)
        checkBox.move(250, 200)
        checkBox.resize(150, 20)
        # checkBox.toggle()
        checkBox.stateChanged.connect(self.enlarge_window)
        self.screen_center = lambda self: QtGui.QApplication.desktop().screen().rect().center() - self.rect().center()
        self.move(self.screen_center(self))

        self.show()
    
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
            self.move(self.screen_center(self))
        else:
            self.setGeometry(50, 50, 500, 500)
            self.move(self.screen_center(self))
    
    def closeEvent(self, QCloseEvent): 
        # Use this when X button is pressed
        QCloseEvent.ignore()
        self.close_application()

    def close_application(self):
        choice = QtGui.QMessageBox.question(self,'Confirmation',
                                            "Sure to exit?",
                                            QtGui.QMessageBox.Yes |
                                            QtGui.QMessageBox.No)
                                # for warning change .questions to .warning
        if choice == QtGui.QMessageBox.Yes:
            print("Exiting Window")
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()