# ConnectFour.py
from collections import namedtuple

Player = namedtuple('Player', ['name', 'color'])

# class Player:
# 	def __init__(self, name, color):
# 		self.name = name 
# 		self.color = color

class Game:
	def __init__(self):
		self.board = [['-' for x in range(7)] for y in range(6)]

	def __repr__(self):
		board = ''
		for row in self.board:
			board += '|'.join(row) + '\n'
		return board

	def get_height(self, position):
		counter = 0
		for i in range(len(self.board)-1, -1, -1):
			find_token = self.board[i][position-1]
			if find_token == '-':
				break
			counter += 1
		return counter

	def move(self, player, position):
		x = position - 1
		y = 5 - self.get_height(position)
		if y < 0:
			raise ValueError('Error: Column full. Choose another')
		self.board[y][x] = player.color

	def calc_winner(self):
		for y in range(len(self.board)-3):
			for x in range(len(self.board[y])-3):
				# chunk = [self.board[y][x:x+4],
				# 		 self.board[y+1][x:x+4],
				# 		 self.board[y+2][x:x+4],
				# 		 self.board[y+3][x:x+4]]
				# print(x, y)
				# for row in chunk:
				# 	print(row)

				# horizontal matches
				for i in range(4): # check all four rows in chunk
					if (self.board[y+i][x] == self.board[y+i][x+1] == self.board[y+i][x+2] == self.board[y+i][x+3]) and self.board[y+i][x] != '-':
						return self.board[y+i][x]

				# vertical match
				if (self.board[y][x] == self.board[y+1][x] == self.board[y+2][x] == self.board[y+3][x]) and self.board[y][x] != '-':
					return self.board[y][x]

				# diagonal matches
				if (self.board[y+3][x] == self.board[y+2][x+1] == self.board[y+1][x+2] == self.board[y][x+3]) and self.board[y][x+3] != '-':
					return self.board[y][x+3]

				if (self.board[y][x] == self.board[y+1][x+1] == self.board[y+2][x+2] == self.board[y+3][x+3]) and self.board[y][x] != '-':
					return self.board[y][x]
		

	def is_full(self):
		for row in self.board:
			for cell in row:
				if cell == '-':
					return False
		return True

	def is_game_over(self):
		return self.calc_winner() or self.is_full()


if __name__ == '__main__':
	game = Game()
	print(game)
	player1 = Player('1', 'Y')
	player2 = Player('2', 'R')
