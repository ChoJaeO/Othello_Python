import change
import undogame

class Othello:
    def __init__(self):
        #1 : white, 2 : black
        self.change = change.Change()
        self.undogame = undogame.UndoTurn()
        self.blackcnt = self.change.getblackcnt()
        self.whitecnt = self.change.getwhitecnt()
        self.board = [[ 0 for i in range(8)] for j in range(8)]

    def MainDrive(self):
        #게임 메인 드라이브
        pass

    def NewGame(self):
        #새 게임 시작 메서드
        self.board = [[ 0 for i in range(8)] for j in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.undogame.setstatus(self.board)

        self.change.setblackcnt(2)
        self.change.setwhitecnt(2)