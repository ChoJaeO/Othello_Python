from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QGridLayout, QTextEdit, QLineEdit, QToolButton, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
import sys
import othello
import change

class OthelloGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.GameName = QLabel()
        self.GameName.setText("Othello Game")

        self.turnstatus = QLabel()
        self.turnstatus.setText("백돌 차례")

        self.gameerror = QLabel()

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

        for i in range(8):
            for j in range(8):
                self.buttonList[i][j].clicked.connect(self.ButtonClicked)
                self.x = i
                self.y = j

        self.undoButton = QPushButton()
        self.undoButton.setText("실행취소")

        self.newgameButton = QPushButton()
        self.newgameButton.setText("새 게임")

        self.settingLayout = QHBoxLayout()
        self.settingLayout.addWidget(self.undoButton)
        self.settingLayout.addWidget(self.newgameButton)

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.GameName, 0, 0)
        mainLayout.addWidget(self.turnstatus, 1, 0)
        mainLayout.addWidget(self.gameerror, 2, 0)
        mainLayout.addLayout(self.statusLayout, 3, 0)
        mainLayout.addLayout(self.buttonLayout, 4, 0)
        mainLayout.addLayout(self.settingLayout, 5, 0)

        self.game = othello.Othello()
        self.game.New_Game()  # 게임을 시작한다
        self.setBoardGUI(self.game.getboard())

        self.setLayout(mainLayout)
        self.setWindowTitle("Othello")

    def ButtonClicked(self):
        self.turnstatus.setText("흑돌 차례" if self.game.turn == 2 else "백돌 차례")
        sender = self.sender()
        for i in range(8):
            for j in range(8):
                if self.buttonList[i][j] == sender:
                    self.x = i
                    self.y = j
                    break
        if self.game.check_proper(self.x, self.y):
            for i in range(8):
                print(self.game.getboard()[i])
            stone_count = 0
            stone_count = self.MainDrive(self.x, self.y)
            self.setBoardGUI(self.game.getboard())
            if stone_count == 64:
                self.gameerror.setText("게임 오버")
        else:
            self.gameerror.setText("올바른 돌을 놓아주세요.")


    def setBoardGUI(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 2:
                    self.buttonList[i][j].setText("●")
                elif board[i][j] == 1:
                    self.buttonList[i][j].setText("○")
                else:
                    self.buttonList[i][j].setText("")
        self.blackstatus.setText(str(self.game.getblack_count()))
        self.whitestatus.setText(str(self.game.getwhite_count()))

    def MainDrive(self, x, y):
        change_Class = change.Change()
        change_count = change_Class.changestones(self.game.getboard(), x, y, self.game.getturn())
        if self.game.getturn() == 1 :
            self.game.setblack_count(change_count + 1)
            self.game.setwhite_count(-change_count)

        elif self.game.getturn() == 2 :
            self.game.setwhite_count(change_count + 1)
            self.game.setblack_count(-change_count)

        self.game.setboard(x, y, self.game.getturn())
        self.game.setturn(3 - self.game.getturn()) ########## 턴 변경 (흑을 둔 뒤엔 백, 백을 둔 뒤엔 흑으로 변경)

        return self.game.getblack_count() + self.game.getwhite_count()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = OthelloGame()
    game.show()
    sys.exit(app.exec_())