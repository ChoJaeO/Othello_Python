class UndoTurn:
    def __init__(self):
        self.i = 0
        self.game_status = [0 for i in range(64)]
        self.game_status[0] = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.cnt_status = [[2, 2],]

    def setstatus(self, new_status):
        self.game_status = new_status

    def addstatus(self, new_status):	#new_status : 최근 게임 판
        #최근 게임 판 추가
        self.i += 1
        print(self.i)
        print("newstatus")
        print(new_status)
        self.game_status[self.i] = new_status
        print(self.game_status[0])
        print(self.game_status[1])
        print(self.game_status[2])

    def getstatus(self):
        #이전 판 반환
        #self.game_status = self.game_status[:-1]
        #print(self.game_status)
        #return self.game_status[-1]
        self.i -= 1
        return self.game_status[self.i]

    def addcntstatus(self, new_cnt_status):
        print(new_cnt_status)
        self.cnt_status += [new_cnt_status]
        print(self.cnt_status)

    def getcntstatus(self):
        self.cnt_status = self.cnt_status[:-1]
        return self.cnt_status[-1]