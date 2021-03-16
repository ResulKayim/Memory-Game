import sys
from random import randint

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

level = int(0)
control = bool(False)
pressed = bool(False)


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setMinimumSize(500, 500)
        self.setMaximumSize(500, 500)
        self.numberList = 0
        self.lenght = 5
        self.showedNumber = 0
        self.setWindowTitle("Memory Game")
        self.setWindowIcon(QIcon("C:\\Users\\Resul\\Desktop\\brain.png"))

        self.levelBig = QtWidgets.QLabel(self)
        self.levelBig.setGeometry(140, 80, 500, 330)
        self.levelBig.setFont(QFont("Time", 300))
        self.levelBig.setStyleSheet('color : rgb(230,230,255);')

        # self.levelBig.move(140,10)
        self.levelBig.setText("0")

        self.Ui()
        # self.show()

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(Qt.black, 1, Qt.SolidLine))

        painter.drawLine(0, 440, 500, 440)
        painter.end()

    def Ui(self):
        self.startButton = QtWidgets.QPushButton(self)
        self.startButton.setFont(QFont("Time", 10))
        self.startButton.setText("START")
        self.startButton.setGeometry(QtCore.QRect(10, 470, 91, 23))

        self.EnterButton = QtWidgets.QPushButton(self)
        self.EnterButton.setFont(QFont("Time", 10))
        self.EnterButton.setText("ENTER")
        self.EnterButton.setGeometry(QtCore.QRect(400, 470, 91, 23))
        self.EnterButton.setEnabled(False)

        self.enterNumber = QtWidgets.QLineEdit(self)
        self.enterNumber.setText("")
        self.enterNumber.setGeometry(QtCore.QRect(110, 470, 281, 22))
        self.enterNumber.setPlaceholderText("Enter Number")
        # self.enterNumber.setValidator(QIntValidator())
        self.enterNumber.setEnabled(False)
        self.enterNumber.setFocusPolicy(Qt.StrongFocus)
        self.enterNumber.setFont(QFont("Time", 10))

        self.message = QtWidgets.QLabel("", self)
        self.message.setText("Initial size of pattern " + str(self.lenght))
        self.message.setFont(QFont("Time", 12))
        self.message.setGeometry(110, 445, 500, 18)

        self.number = QtWidgets.QLabel(self)
        self.number.setFont(QFont("Time", 18))
        self.number.setGeometry(100, 100, 100, 100)
        self.number.setText("")

        self.userLevel = 1

        '''self.levelLabel = QtWidgets.QLabel(self)
        self.levelLabel.setText("LEVEL : 1")
        self.levelLabel.setFont(QFont("Time", 12))
        self.levelLabel.setStyleSheet('color : darkRed')
        self.levelLabel.move(10,445)'''

        self.startButton.clicked.connect(self.start)
        self.EnterButton.clicked.connect(self.Enter)

        # self.show()
        # self.enterNumber.returnPressed.connect(self.Enter)

        '''self.number.move(250,100)
        self.number.setText("9")'''

    def start(self):
        global level, control, pressed
        if control:
            self.number.setText("")
            self.message.setText("Enter what you remember(Only Number)")
            self.startButton.setText("START")
            self.enterNumber.setEnabled(True)
            self.EnterButton.setEnabled(True)
            self.startButton.setEnabled(False)
            self.showedNumber = 0
            self.timer.stop()
            self.enterNumber.setFocus()
            control = False
            pressed = True
            print(self.numberList)
        else:
            self.message.setText("Try To Focus On")
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.showNumber)
            self.timer.start(level)
            self.enterNumber.setMaxLength(self.lenght)
            self.EnterButton.setEnabled(False)
            self.enterNumber.setEnabled(False)
            self.startButton.setEnabled(True)
            self.startButton.setText("STOP")
            self.enterNumber.setText("")
            # self.message.setText("")
            control = True

    def showNumber(self):
        global control
        if self.showedNumber != self.lenght:
            i = randint(1, 9)
            self.number.setText(str(i))
            self.number.move(randint(1, 484), randint(1, 375))
            self.showedNumber += 1
            self.numberList = self.numberList * 10 + i
        else:
            self.number.setText("")
            self.message.setText("Enter what you remember(Only Number)")
            self.enterNumber.setEnabled(True)
            self.EnterButton.setEnabled(True)
            self.startButton.setEnabled(False)
            control = False
            self.showedNumber = 0
            self.timer.stop()
            self.enterNumber.setFocus()
            print(self.numberList)

    def Enter(self):
        global control, pressed
        # self.message.setText("")
        try:
            text = self.enterNumber.text()

            if text == "":
                self.message.setText("Please Enter Numbers")

            else:
                number = int(text)

                if number == self.numberList:
                    self.message.setText("You know")
                    if not pressed:
                        self.lenght += 1
                        self.userLevel += 1

                        # self.levelLabel.setText("LEVEL : " + str(self.userLevel))
                        self.levelBig.setText(str(self.userLevel))
                        if self.userLevel > 9:
                            self.levelBig.setGeometry(50, 80, 500, 330)

                    self.start()
                    self.numberList = 0
                    print("/*//*/*/*/*/*/*/*/*/*/*/*/**/*//*/*/**/")
                    # self.startButton.setEnabled(True)
                else:
                    self.message.setText("You Failed Number :" + str(self.numberList))
                    self.lenght = 5
                    self.EnterButton.setEnabled(False)
                    # self.startButton.setEnabled(True)
                    self.numberList = 0
                    self.enterNumber.setText("")
                    self.enterNumber.setEnabled(False)
                    self.startButton.setText("START")
                    self.startButton.setEnabled(True)
                    print("/*//*/*/*/*/*/*/*/*/*/*/*/**/*//*/*/**/")
                pressed = False
        except ValueError:
            self.message.setText("Please Only NUMBER")
            self.enterNumber.selectAll()

    def keyPressEvent(self, QKeyEvent):
        key = QKeyEvent.key()
        if key == Qt.Key_Enter or key == 16777220:
            if self.startButton.isEnabled():
                self.start()
            elif self.EnterButton.isEnabled():
                self.Enter()


class Level(QtWidgets.QWidget):
    def __init__(self):
        super(Level, self).__init__()
        self.setWindowTitle("Select Memory Game Level")
        self.setMinimumSize(400, 100)
        self.setMaximumSize(400, 100)
        self.setWindowIcon(QIcon("C:\\Users\\Resul\\Desktop\\brain.png"))

        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(p)

        self.setUi()

    def setUi(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("PLEASE CHOOSE LEVEL")
        self.label.setGeometry(120, 10, 300, 20)
        self.label.setFont(QFont("Time", 12))

        self.low = QtWidgets.QRadioButton(self)
        self.low.setText("LOW")
        self.low.move(30, 40)
        self.low.setStyleSheet(
            'QRadioButton{font: 13pt Helvetica MS;} QRadioButton::indicator { width: 13px; height: 20px;}')

        self.medium = QtWidgets.QRadioButton(self)
        self.medium.setText("MEDIUM")
        self.medium.move(90, 40)
        self.medium.setChecked(True)
        self.medium.setStyleSheet(
            'QRadioButton{font: 13pt Helvetica MS;} QRadioButton::indicator { width: 13px; height: 20px;}')

        self.hard = QtWidgets.QRadioButton(self)
        self.hard.setText("HARD")
        self.hard.move(185, 40)
        self.hard.setStyleSheet(
            'QRadioButton{font: 13pt Helvetica MS;} QRadioButton::indicator { width: 13px; height: 20px;}')

        self.vHard = QtWidgets.QRadioButton(self)
        self.vHard.setText("VERY HARD")
        self.vHard.move(265, 40)
        self.vHard.setStyleSheet(
            'QRadioButton{font: 13pt Helvetica MS;} QRadioButton::indicator { width: 13px; height: 20px;}')

        self.button = QtWidgets.QPushButton(self)
        self.button.setText("SELECT")
        self.button.setGeometry(150, 70, 100, 20)
        self.button.setStyleSheet("background-color: darkCyan")
        self.button.clicked.connect(self.play)
        self.button.setFont(QFont("Time", 11))

        self.show()

    def play(self):
        global level, wind
        if self.low.isChecked():
            level = 2000
            wind.show()
            self.hide()
        elif self.medium.isChecked():
            level = 1500
            wind.show()
            self.hide()
        elif self.hard.isChecked():
            level = 1000
            wind.show()
            self.hide()
        elif self.vHard.isChecked():
            level = 500
            wind.show()
            self.hide()
        else:
            self.label.setStyleSheet('color : darkRed')
            self.label.setText("!!! CHOOSE ONE !!!")

    def keyPressEvent(self, QKeyEvent):
        self.play()


app = QtWidgets.QApplication(sys.argv)

level = Level()
wind = Window()

sys.exit(app.exec())
