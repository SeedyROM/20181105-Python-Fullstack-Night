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

	def hidden_cards(self):
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


	def print_hand_and_score(self, player, hidden=False):
		if hidden:
			hand = player.hidden_cards()
			score = f'Visible score: {player.visible_score()}'
		else:
			hand = str(player)
			score = f'Visible score: {player.score()}'

		print()
		print('-'*58)
		print(f"{player.name}'s hand:")
		print('-'*58)
		print(hand)
		print()
		print(score)
		print('-'*58)


	def play(self):
		game_over = False
		while not game_over:
			self.print_hand_and_score(self.dealer, hidden=True)
			players_moves = []

			# ask players' moves
			for i in range(len(self.players)):
				player = self.players[i]
				if player.game_over:
					print(f'\n{player.name}: {player.game_over}\n')
					continue

				self.print_hand_and_score(player)

				while True:
					move = input('(h)it or (s)tay: ').strip().lower()
					if move in ['h', 'hit', 's', 'stay']:
						if move.startswith('h'):
							card = self.deck.draw()	# draw card from top of deck
							player.add(card)		# add card to player's hand
							print(f'\n{card}\n')
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
			self.print_hand_and_score(self.dealer, hidden=True)

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
		self.print_hand_and_score(self.dealer, hidden=False)

		# Calculate winner
		for player in self.players:
			self.print_hand_and_score(player)

			if player.score() > 21:
				print(player.name + ' busted!')
			elif player.score() == self.dealer.score():
				print(player.name + ' pushes')
			elif player.score() < self.dealer.score() <= 21:
				print(player.name + ' loses')
			else:
				print(player.name + ' wins!')

			print('-'*58)




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