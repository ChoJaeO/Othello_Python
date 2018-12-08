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
        while True:
            self.coordinate_x = int(input("x좌표를 입력하세요."))
            self.coordinate_y = int(input("y좌표를 입력하세요."))
            if self.check_proper():
                break
        coordinate = (self.coordinate_x, self.coordinate_y)
        self.change.changestones(self.board, coordinate, self.color)
        self.color = 3-self.color

    def NewGame(self):
        #새 게임 시작 메서드
        self.board = [[ 0 for i in range(8)] for j in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.undogame.setstatus(self.board)

        self.color = 1

        self.change.setblackcnt(2)
        self.change.setwhitecnt(2)

    def check_proper(self):
        range_0 = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        xy_status = False
        for i , j in range_0:
            try:
                if self.board[self.coordinate_x + i][self.coordinate_y + j] != 0:
                    xy_status = True
                    print(xy_status)
                    break
            except IndexError:
                pass
        if not xy_status:
            return xy_status

        return self.board[self.coordinate_x][self.coordinate_y] == 0

    def Game_Over(self):
        for i in self.board:
            if 0 in i:
                return False
        else:
            return True

if __name__ == '__main__':
    game = Othello()
    game.NewGame()
    print(game.board)
    while not game.Game_Over():
        game.MainDrive()
        print(game.board)