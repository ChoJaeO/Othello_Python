class Change:
    def __init__(self):
        self.blackcnt = 2
        self.whitecnt = 2

    def changestones(self, board, stone_location, color):	#stone_location : 흑돌 백돌 좌표값
        #흑돌 백돌 뒤집는 메서드
        x = stone_location[0]
        y = stone_location[1]
        self.board = board

        if color in self.board[x][y+1:]:
            for i in range(y+1, 8, 1):
                if self.board[x][i] == color:
                    break
                self.board[x][i] = 3-self.board[x][i]
        if color in self.board[x][:y]:
            for i in range(y-1, -1, -1):
                if self.board[x][i] == color:
                    break
                self.board[x][i] = 3-self.board[x][i]
        if color in [self.board[i][y] for i in range(x+1,8)]:
            for j in range(x+1, 8, 1):
                if self.board[j][y] == color:
                    break
                self.board[j][y] = 3 - self.board[j][y]
        if color in [self.board[i][y] for i in range(x)]:
            for j in range(x-1, -1, -1):
                if self.board[j][y] == color:
                    break
                self.board[j][y] = 3 - self.board[j][y]
        self.board[x][y] = color

    def getresult(self):
        #결과값 반환 메서드 - 리스트 형태(좌표 형태)
        return self.board

    def getblackcnt(self):
        #흑돌 개수 반환 메서드
        return self.blackcnt

    def setblackcnt(self, n):
        self.blackcnt = n

    def getwhitecnt(self):
        #백돌 개수 반환 메서드
        return self.whitecnt

    def setwhitecnt(self, n):
        self.whitecnt = n