class UndoTurn:
    def __init__(self):
        self.game_status = []

    def setstatus(self, new_status):
        self.game_status = new_status

    def addstatus(self, new_status):	#new_status : 최근 게임 판
        #최근 게임 판 추가
        self.game_status.append(new_status)

    def getstatus(self):
        #이전 판 반환
        return self.game_status.pop()