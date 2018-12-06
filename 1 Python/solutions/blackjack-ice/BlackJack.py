# BlackJack.py
from Deck import Deck

class Hand:
	def __init__(self, card1, card2, name):
		self.cards = [card1, card2] 
		self.name = name
		self.game_over = False

	def __repr__(self):
		return str(self.cards)

	def add(self, card):
		self.cards.append(card) 

	def score(self):
		points = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
		total = 0
		for card in self.cards:
			total += points[card.rank]
		return total


class Dealer(Hand):
	def __init__(self, card1, card2):
		super().__init__(card1, card2, name='Dealer')

	def __repr__(self):
		hidden_card = 'Hidden Card'
		cards = [hidden_card] + self.cards[1:]
		return str(cards)		

	def visible_score(self):
		points = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
		total = 0
		cards = self.cards[1:]
		for card in cards:
			total += points[card.rank]
		return total

	def reveal_cards(self):
		print(self.cards)


class Game:
	def __init__(self, num_players=1):
		self.deck = Deck()		# create deck
		self.deck.shuffle()		# shuffle deck
		self.deck.cut()			# cut deck
		self.players = []
		# create dealer and draw two cards
		self.dealer = Dealer(self.deck.draw(), self.deck.draw())	
		# create players and draw two cards each
		for i in range(num_players):
			name = input(f'Enter name for player {i+1}: ')
			player = Hand(self.deck.draw(), self.deck.draw(), name)
			self.players.append(player)


	def game_over(self, player):
		score = player.score()
		if score > 21:
			return 'Busted'
		elif score == 21:
			return 'Blackjack!'
		return False


	def play(self):
		game_over = False
		while not game_over:
			print()
			print(f"Dealer's hand: {self.dealer}")
			print(f"Dealer's visible score: {self.dealer.visible_score()}")
			players_moves = []

			# ask players' moves
			for i in range(len(self.players)):
				player = self.players[i]
				if player.game_over:
					print(player.game_over)
					continue

				print()	
				print(f"{player.name}'s hand: {player}")	
				print(f"{player.name}'s score: {player.score()}")

				while True:
					move = input('(h)it or (s)tay: ').strip().lower()
					if move in ['h', 'hit', 's', 'stay']:
						if move.startswith('h'):
							card = self.deck.draw()	# draw card from top of deck
							player.add(card)		# add card to player's hand
							print(card)
							# check if game is over for the player
							player.game_over = self.game_over(player)
							if player.game_over:
								print(player.game_over)
								break
						else:
							break

				players_moves.append(move)

			# calculate dealer's move
			score = self.dealer.score()
			print()
			print(f"Dealer's hand: {self.dealer}")
			print(f"Dealer's visible score: {self.dealer.visible_score()}")

			if (17 <= score < 21):
				print('Dealer stays')
			else: # dealer hits
				print('Dealer hits')
				card = self.deck.draw()	# draw card from top of deck
				self.dealer.add(card) 	# add card to dealer's hand
				print(card)				
				self.dealer.game_over = self.game_over(self.dealer)	
				if self.dealer.game_over:
					print(self.game_over(self.dealer))
					break

			if ('hit' not in players_moves) and ('h' not in players_moves):
				game_over = True

			if len(players_moves) == 0:
				game_over = True

		# Reveal dealer's hand
		print()
		print("Dealer's hand: ")
		self.dealer.reveal_cards()
		print(f"Dealer's score: {self.dealer.score()}")

		# Calculate winner
		for player in self.players:
			print()	
			print(f"{player.name}'s hand: {player}")	
			print(f"{player.name}'s score: {player.score()}")

			if player.score() > 21:
				print(player.name + ' busted!')
			elif player.score() == self.dealer.score():
				print(player.name + ' pushes')
			elif player.score() < self.dealer.score() <= 21:
				print(player.name + ' loses')
			else:
				print(player.name + ' wins!')




if __name__ == '__main__':
	# num_players = input('How many players: ')
	game = Game(2)
	game.play()
	# for player in game.players:
	# 	print(player)
	# 	print(player.score())

	# print(game.dealer)
	# print(game.dealer.visible_score())
	# print(game.dealer.score())