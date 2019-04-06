import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QFontDialog, QStyleFactory, QLabel

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Why aren't you using i3?")
        self.styleChoice = QLabel("Windows Vista", self)
        # self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        extractAction = QAction("&Quit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave the App')
        extractAction.triggered.connect(self.close_application)
        fontChoice = QAction('&Font', self)
        fontChoice.triggered.connect(self.font_choice)
        style = QAction('&Style', self)
        style.triggered.connect(self.style_choice)


        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&file')
        fileMenu.addAction(extractAction)
        editMenu = mainMenu.addMenu('&edit')
        editMenu.addAction(fontChoice)
        editMenu.addAction(style)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        #btn.resize(100, 100)
        btn.move(0, 100)
        self.show()

    def style_choice(self, text):
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    def font_choice(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    def close_application(self):
        print("hey bitch")
        sys.exit()

def run():
    app = QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
