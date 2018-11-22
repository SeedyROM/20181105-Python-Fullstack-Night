# pick6_ice.py
import random 

def pick6():
	ticket = []
	for i in range(6):
		ticket.append(random.randint(1,99))
	return ticket

def num_matches(winning, ticket):
	matches = 0
	for i in range(len(ticket)):
		if winning[i] == ticket[i]:
			matches += 1
	return matches 

def play100k():
	winning = pick6()
	balance = 0
	earnings = 0
	winnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
	# # alternative to above
	# winnings = {0: 0, 1: 4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

	for i in range(100000):
		ticket = pick6()
		balance -= 2
		matches = num_matches(winning, ticket)
		payout = winnings[matches]
		balance += payout
		earnings += payout

		if matches > 3:
			print(winning)
			print(ticket)
			print(f'Won ${payout}')		
		
	roi = (earnings - 200000)/200000
	print(f'Final balance: {balance}')
	print(f'ROI: {roi}')


for i in range(100):
	play100k()
