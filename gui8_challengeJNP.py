""" A Jack and Poy game """

import sys
import random as r
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super (Window, self).__init__()
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle("CLMITS Rocks!")
        self.setWindowIcon(QtGui.QIcon('images/python.png'))

        self.options = {1:"Rock",2:"Paper",3:"Scissors"}
        self.home()
    
    def home(self):
        self.winnerlbl = QtGui.QLabel("Winner", self)
        self.winnerlbl.setGeometry(90, 70, 500,100)

        rockbtn = QtGui.QPushButton("Rock", self)
        rockbtn.clicked.connect(lambda: self.jack_en_poy('1'))
        rockbtn.move(70, 250)

        paperbtn = QtGui.QPushButton("Paper", self)
        paperbtn.clicked.connect(lambda: self.jack_en_poy('2'))
        paperbtn.move(200, 250)

        scissorsbtn = QtGui.QPushButton("Scissors", self)
        scissorsbtn.clicked.connect(lambda: self.jack_en_poy('3'))
        scissorsbtn.move(330, 250)
        self.show()
    
    def jack_en_poy(self,user_choice):
        choice = int(user_choice)
        random_choice = r.randint(1,3)
        if(choice == random_choice):
            self.winnerlbl.setText(f"Draw - Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print(f"Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print("Draw")
        elif( (choice == 1 and random_choice == 2) or (choice == 2 and random_choice == 3) or (choice == 3 and random_choice == 1)):
            self.winnerlbl.setText(f"You Lose - Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print(f"Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print("Player lose")
        else:
            self.winnerlbl.setText(f"You Win - Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print(f"Player chose {self.options[choice]} and Opponent chose {self.options[random_choice]}")
            print("Player wins")

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()