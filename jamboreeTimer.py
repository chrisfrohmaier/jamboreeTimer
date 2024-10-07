# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
from playsound import playsound
import glob
import random
import time
import argparse

## Defining the path to the mp3 folder
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help="Path to the directory containing the MP3 files to randomly play.")

# Execute the parse_args() method
args = parser.parse_args()
mp3Path = args.path
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Astro Jamboree Timer")
  
        # setting geometry
        # setGeometry(left, top, width, height)
        self.setGeometry(100, 100, 1200, 800)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
    # method for widgets
    def UiComponents(self):
  
        # variables
        # count variable
        self.count = 0
  
        # start flag
        self.start = False

        ##!!! SET CUSTOM TIME
        # creating push button to get time in seconds
        button = QPushButton("Set custom", self)
  
        # setting geometry to the push button
        button.setGeometry(50, 50, 300, 100)
        button.setFont(QFont('Helvetica', 36))
        # adding action to the button
        button.clicked.connect(self.get_seconds)

        ##!!! SET ONE MIN TIME
        # creating push button to get time in seconds
        oMINbutton = QPushButton("Start 1 minute", self)
  
        # setting geometry to the push button
        oMINbutton.setGeometry(450, 50, 300, 100)
        oMINbutton.setFont(QFont('Helvetica', 36))
        # adding action to the button
        oMINbutton.clicked.connect(self.start_OneMin)

        ##!!! SET TWO MIN TIME
        # creating push button to get time in seconds
        twoMINbutton = QPushButton("Start 2 minutes", self)
  
        # setting geometry to the push button
        twoMINbutton.setGeometry(850, 50, 300, 100)
        twoMINbutton.setFont(QFont('Helvetica', 36))
        # adding action to the button
        twoMINbutton.clicked.connect(self.start_TwoMin)
  

        ## ADDING THE TIMER DISPLAY
        # creating label to show the seconds
        self.label = QLabel("0.0 s", self)
  
        # setting geometry of label
        self.label.setGeometry(50, 170, 1100, 460)
  
        # setting border to the label
        self.label.setStyleSheet("border : 3px solid white")
  
        # setting font to the label
        self.label.setFont(QFont('Helvetica', 325))
  
        # setting alignment ot the label
        self.label.setAlignment(Qt.AlignCenter)
  

        ## ADDING THE LOWER BUTTONS

        ##START
        # creating start button
        start_button = QPushButton("Start", self)
  
        # setting geometry to the button
        start_button.setGeometry(50, 650, 260, 100)
        start_button.setFont(QFont('Helvetica', 36))
        # adding action to the button
        start_button.clicked.connect(self.start_action)
  
        ##PAUSE
        # creating pause button
        pause_button = QPushButton("Pause", self)
  
        # setting geometry to the button
        pause_button.setGeometry(330, 650, 260, 100)
        pause_button.setFont(QFont('Helvetica', 36))
  
        # adding action to the button
        pause_button.clicked.connect(self.pause_action)
  
        ## RESET BUTTON
        # creating reset  button
        reset_button = QPushButton("Reset", self)
  
        # setting geometry to the button
        reset_button.setGeometry(610, 650, 260, 100)
        reset_button.setFont(QFont('Helvetica', 36))
  
        # adding action to the button
        reset_button.clicked.connect(self.reset_action)

        ## RESET BUTTON
        # creating reset  button
        arnie_button = QPushButton("Random 🎵", self)
  
        # setting geometry to the button
        arnie_button.setGeometry(885, 650, 260, 100)
        arnie_button.setFont(QFont('Helvetica', 36))
  
        # adding action to the button
        arnie_button.clicked.connect(self.arnie_action)
  
        # creating a timer object
        timer = QTimer(self)
  
        # adding action to timer
        timer.timeout.connect(self.showTime)
  
        # update the timer every tenth second
        timer.start(100)
  
    # method called by timer
    def showTime(self):
  
        # checking if flag is true
        if self.start:
            # incrementing the counter
            self.count -= 1
  
            # timer is completed
            if self.count == 0:
  
                # making flag false
                self.start = False
  
                # setting text to the label
                self.label.setText("0.0 s")
                #time.sleep(0.1)
                self.arnie_action()

                ## ADD PLAY SOUND HERE
  
        if self.start:
            # getting text from count
            text = str(self.count / 10) + " s"
  
            # showing text
            self.label.setText(text)
  
  
    # method called by the push button
    def get_seconds(self):
  
        # making flag false
        self.start = False
  
        # getting seconds and flag
        second, done = QInputDialog.getInt(self, 'Seconds', 'Enter Seconds:')
  
        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10
  
            # setting text to the label
            self.label.setText(str(second))

        # method called by the push button
    def start_OneMin(self):
  
        # making flag false
        self.start = False
  
        # getting seconds and flag
        second = 60
        done = True
  
        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10
  
            # setting text to the label
            self.label.setText(str(second))
            self.start_action()
    
    def start_TwoMin(self):
  
        # making flag false
        self.start = False
  
        # getting seconds and flag
        second = 120
        done = True
  
        # if flag is true
        if done:
            # changing the value of count
            self.count = second * 10
  
            # setting text to the label
            self.label.setText(str(second))
            self.start_action()
  
    def start_action(self):
        # making flag true
        self.start = True
  
        # count = 0
        if self.count == 0:
            self.start = False
  
    def pause_action(self):
  
        # making flag false
        self.start = False
    
    def arnie_action(self):
        #Add the random Arnie noise here
        #print('Arnie sound')
        playsound(random.choice(arnie_files))
    
    def reset_action(self):
  
        # making flag false
        self.start = False
  
        # setting count value to 0
        self.count = 0
  
        # setting label text
        self.label.setText("0.0 s")


##get the Arnie sounds

arnie_path = mp3Path    
arnie_files = glob.glob(arnie_path+'*.mp3')
#print(arnie_files)

# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())