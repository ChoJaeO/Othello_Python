from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QGridLayout, QTextEdit, QLineEdit, QToolButton, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
import sys

class OthelloGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.GameName = QLabel()
        self.GameName.setText("Othello Game")

        self.blackplayer = QLabel()
        self.blackplayer.setText("●")
        self.whiteplayer = QLabel()
        self.whiteplayer.setText("○")
        self.blackstatus = QLabel()
        self.blackstatus.setText(str(2))
        self.whitestatus = QLabel()
        self.whitestatus.setText(str(2))

        self.statusLayout = QHBoxLayout()
        self.statusLayout.addWidget(self.blackplayer)
        self.statusLayout.addWidget(self.blackstatus)
        self.statusLayout.addWidget(self.whiteplayer)
        self.statusLayout.addWidget(self.whitestatus)

        self.buttonList = [[QToolButton() for i in range(8)] for j in range(8)]

        self.buttonLayout = QGridLayout()
        for i in range(8):
            for j in range(8):
                self.buttonLayout.addWidget(self.buttonList[i][j], i, j)

        self.undoButton = QPushButton()
        self.undoButton.setText("실행취소")

        self.newgameButton = QPushButton()
        self.newgameButton.setText("새 게임")

        self.settingLayout = QHBoxLayout()
        self.settingLayout.addWidget(self.undoButton)
        self.settingLayout.addWidget(self.newgameButton)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.GameName, 0, 0)
        mainLayout.addLayout(self.statusLayout, 1, 0)
        mainLayout.addLayout(self.buttonLayout, 2, 0)
        mainLayout.addLayout(self.settingLayout, 3, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Othello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = OthelloGame()
    game.show()
    sys.exit(app.exec_())