class Change:
    def __init__(self):
        self.can_change = 0 ##### 돌의 색을 바꿀 수 있는 조건을 만족하면 1
        self.changing = 0 ##### 이번턴에 바뀐 돌의 개수

    def check(self, board, x, y, direction_x, direction_y, c):
        self.board = board
        check_x = x + direction_x
        check_y = y + direction_y

        if check_x == -1 or check_x == 8 or check_y == -1 or check_y == 8 or self.board[check_x][check_y] == 0 :
            return

        elif self.board[check_x][check_y] == 3 - c :
            self.check(self.board, check_x, check_y, direction_x, direction_y, c)
            if self.can_change == 1 :
                self.board[check_x][check_y] = c
                self.changing += 1

        elif self.board[check_x][check_y] == c :
            self.can_change = 1
            return

    def changestones(self, board, x, y, color):	#stone_location : 흑돌 백돌 좌표값
        #흑돌 백돌 뒤집는 메서드
        self.board = board
        eight_direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]] ##### 8방향

        self.changing = 0
        for i in range(8) :
            self.can_change = 0
            self.check(self.board, x, y, eight_direction[i][0], eight_direction[i][1], color)

        return self.changing
