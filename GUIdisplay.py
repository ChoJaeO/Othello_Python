from PyQt5.QtWidgets import (QApplication, QWidget, QLayout, QGridLayout, QTextEdit, QLineEdit, QToolButton, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from PyQt5.QtCore import Qt
import sys
import othello
import change
import undogame

class OthelloGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.GameName = QLabel()
        self.GameName.setText("Othello Game")
        self.GameName.setAlignment(Qt.AlignCenter)

        self.turnstatus = QLabel()
        self.turnstatus.setText("흑돌 차례")
        self.turnstatus.setAlignment(Qt.AlignCenter)

        self.gameerror = QLabel()
        self.gameerror.setAlignment(Qt.AlignCenter)

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
        self.undogame = undogame.UndoTurn()
        self.newgameButton.clicked.connect(self.settingNewGame)
        self.undoButton.clicked.connect(self.UndoGame)
        self.game.New_Game()  # 게임을 시작한다
        self.setBoardGUI(self.game.getboard())

        self.setLayout(mainLayout)
        self.setWindowTitle("Othello")

    def UndoGame(self):
        try:
            self.gameerror.setText("")
            self.game.undoboard(self.undogame.getstatus())
            print(self.game.getboard())
            self.setBoardGUI(self.game.getboard())
            a = self.undogame.getcntstatus()
            print(a)
            self.game.setblack_count(a[0])
            self.game.setwhite_count(a[1])
            self.blackstatus.setText(str(self.game.getblack_count()))
            self.whitestatus.setText(str(self.game.getwhite_count()))
            self.game.setturn(3-self.game.getturn())
            self.turnstatus.setText("흑돌 차례" if self.game.getturn() == 1 else "백돌 차례")

        except IndexError:
            self.gameerror.setText("더이상 뒤로 갈수 없습니다.")
            self.undogame = undogame.UndoTurn()

    def settingNewGame(self):
        self.undogame = undogame.UndoTurn()
        self.gameerror.setText("")
        self.game.New_Game()
        self.setBoardGUI(self.game.getboard())
        self.blackstatus.setText("2")
        self.whitestatus.setText("2")
        self.turnstatus.setText("흑돌 차례" if self.game.getturn() == 1 else "백돌 차례")

    def ButtonClicked(self):
        self.gameerror.setText("")
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
            stone_count = self.MainDrive(self.x, self.y)
            self.setBoardGUI(self.game.getboard())

            self.undogame.addstatus(self.game.getboard())
            self.undogame.addcntstatus([self.game.getblack_count(), self.game.getwhite_count()])

            self.turnstatus.setText("흑돌 차례" if self.game.getturn() == 1 else "백돌 차례")
            if stone_count == 64:
                self.gameerror.setText("게임 오버")
                self.turnstatus.setText("흑돌 승" if self.game.getwhite_count() < self.game.getblack_count() else "백돌 승")

        else:
            self.gameerror.setText("올바른 돌을 놓아주세요.")


    def setBoardGUI(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == 1:
                    self.buttonList[i][j].setText("●")

                elif board[i][j] == 2:
                    self.buttonList[i][j].setText("○")

                else:
                    self.buttonList[i][j].setText("")

        self.blackstatus.setText(str(self.game.getblack_count()))
        self.whitestatus.setText(str(self.game.getwhite_count()))

    def MainDrive(self, x, y):
        change_Class = change.Change()
        change_count = change_Class.changestones(self.game.getboard(), x, y, self.game.getturn())

        if(change_count == 0) :
            # 돌을 넣을수 없다는 라벨 출력
            self.gameerror.setText("올바른 돌을 놓아주세요")

        else :
            if self.game.getturn() == 1:
                self.game.addblack_count(change_count + 1)
                self.game.addwhite_count(-change_count)

            elif self.game.getturn() == 2 :
                self.game.addblack_count(-change_count)
                self.game.addwhite_count(change_count + 1)


            self.game.setboard(x, y, self.game.getturn())
            self.game.setturn(3 - self.game.getturn()) ########## 턴 변경 (흑을 둔 뒤엔 백, 백을 둔 뒤엔 흑으로 변경)

        return self.game.getblack_count() + self.game.getwhite_count()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = OthelloGame()
    game.show()
    sys.exit(app.exec_())