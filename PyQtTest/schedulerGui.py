import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    #grid.setColumnStretch(1, 4)
    #grid.setColumnStretch(2, 4)
    #grid.setColumnStretch(0, .1)

    # for i in range(0, 147, 3): # actual final range
    for i in range(0, 24, 3): # test range
        for j in range(0, 9):
            if i == 0:
                if j == 0:
                    item = QLabel("")
                if j == 1:
                    item = QLabel("Sunday")
                if j == 2:
                    item = QLabel("Monday")
                if j == 3:
                    item = QLabel("Tuesday")
                if j == 4:
                    item = QLabel("Wednesday")
                if j == 5:
                    item = QLabel("Thursday")
                if j == 6:
                    item = QLabel("Friday")
                if j == 7:
                    item = QLabel("Saturday")
                item.setAlignment(Qt.AlignCenter)
                item.setStyleSheet("""
                    .QLabel {
                        /*background-color: rgb(255, 255, 255);*/
                    }
                    """)
                grid.addWidget(item, i, j, 1, 1)
            elif j == 0 or j == 8:
                item = QLabel(str(((i - 3)//3) // 2) + ":" + ("30" if ((i - 3)//3) % 2 else "00"))
                item.setStyleSheet("""
                    .QLabel {
                        /*background-color: rgb(255, 255, 255);*/
                    }
                """)
                item.setWordWrap(True)
                item.setAlignment(Qt.AlignCenter)
                grid.addWidget(item, i, j, 3, 1)
            else:
                item = QLabel("B" + str(i//3) + str(j))
                item.setWordWrap(True)
                item.setAlignment(Qt.AlignCenter)
                item.setStyleSheet("""
                    .QLabel {
                        background-color: rgb(255, 0, 0);
                        margin-top: 10px;
                        margin-bottom: 10px;
                        margin-right: 10px;
                        margin-left: 10px;
                    }
                    """)
                grid.addWidget(item, i, j, 3, 1)
			
    win.setLayout(grid)
    win.setGeometry(100,100,200,100)
    win.setWindowTitle("Why aren't you using i3?")
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
