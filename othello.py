import change
import undogame

class Othello:
    def __init__(self):
        self.change = change.Change()
        self.undogame = undogame.UndoTurn()
        self.black_count = 0 ##### 현재 흑돌의 개수
        self.white_count = 0 ##### 현재 백돌의 개수
        self.board = [[ 0 for i in range(8)] for j in range(8)] ###### 게임판  (0은 빈칸, 1은 흑돌, 2는 백돌)
        self.turn = 1 ##### 현재 턴 (흑 선공)

    def New_Game(self):
        #새 게임 시작 메서드
        self.board = [[ 0 for i in range(8)] for j in range(8)] ##### 판 초기화
        self.board[3][3] = self.board[4][4] = 1
        self.board[3][4] = self.board[4][3] = 2 ##### 게임 초기의 판은 흑돌 백돌 2개가 판의 가운데서 서로 엇갈려있는 상태
        self.black_count = self.white_count = 2

        self.undogame.setstatus(self.board)

    def Main_Drive(self): # 돌을 둘 좌표 입력 및 게임 진행
        #게임 메인 드라이브
        while True:
            print("흑 돌의 개수 : %d   백 돌의 개수 : %d" %(self.black_count, self.white_count))
            self.put_x = int(input("x좌표를 입력하세요."))
            self.put_y = int(input("y좌표를 입력하세요."))
            if self.check_proper():
                break

        self.board[self.put_x][self.put_y] = self.turn
        change_count = self.change.changestones(self.board, self.put_x, self.put_y, self.turn)
        if self.turn == 1 :
            self.black_count += change_count + 1
            self.white_count -= change_count

        elif self.turn == 2 :
            self.black_count -= change_count
            self.white_count += change_count + 1

        self.turn = 3 - self.turn ########## 턴 변경 (흑을 둔 뒤엔 백, 백을 둔 뒤엔 흑으로 변경)
        return self.black_count + self.white_count

    def check_proper(self):
        range_0 = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        xy_status = False
        for i , j in range_0:
            try:
                if self.board[self.put_x + i][self.put_y + j] != 0:
                    xy_status = True
                    print(xy_status)
                    break

            except IndexError:
                pass

        if not xy_status:
            return xy_status

        return self.board[self.put_x][self.put_y] == 0

    def End_Game(self): ##### 게임이 종료된 후 승패 결정
        print("흑 돌의 개수 : %d    백 돌의 개수 : %d" %(self.black_count, self.white_count))
        if self.black_count > self.white_count :
            print("흑 승리!!")

        elif self.black_count < self.white_count :
            print("백 승리!!")

        else :
            print("무승부!!")

if __name__ == '__main__':
    game = Othello()
    game.New_Game() # 게임을 시작한다
    for i in range(8) :
        print(game.board[i])

    stone_count = 0
    while stone_count != 64:
        stone_count = game.Main_Drive()
        for i in range(8) :
            print(game.board[i])

    game.End_Game()