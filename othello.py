class Othello:
	def __init__(self):
		self.board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,2,1,0,0,0],[0,0,0,1,2,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
		self.black_cnt = 2
		self.white_cnt = 2
		self.black_input
		self.white_input
		self.turn = True
		self.turn_color = 1
		self.black_x
		self.black_y
		self.white_x
		self.white_y

	def game(self):
		if turn:
			self.black_input = input("흑돌 놓을 곳을 정해주세요.")
			self.black_x = int(self.black_input[0])
         	self.black_y = int(self.black_input[1])
         	turn_color = 1
		else:
			self.white_input = input("백돌 놓을 곳을 정해주세요.")
			self.white_x = int(self.white_input[0])
			self.white_y = int(self.white_input[1])
			turn_color = 2
		
		turn = not turn

		for i in range(black_x+1, 8):
			if self.board[i][black_y] == 1:
				self.board[j for j in range()][black_y]
			pass

		for i in range(0,black_x):
			pass

		for i in range(black_y+1, 8):
			pass

		for i in range(0, black_y):
			pass






		
