class Change:
    def __init__(self):
        self.blackcnt = 2
        self.whitecnt = 2

    def changestones(self, stone_location):	#stone_location : 흑돌 백돌 좌표값
        #흑돌 백돌 뒤집는 메서드
        pass

    def getresult(self):
        #결과값 반환 메서드 - 리스트 형태(좌표 형태)
        pass

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