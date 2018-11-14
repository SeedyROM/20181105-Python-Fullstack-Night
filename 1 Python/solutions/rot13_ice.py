# rot13_ice.py
ENGLISH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
ROT_13 =  'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

def decode(string):
	decoded = ''
	for i in range(len(string)):
		rotated_idx = ROT_13.find(string[i])
		if (rotated_idx) > -1:
			decoded += ENGLISH[rotated_idx]
		else:
			decoded += string[i]
	return decoded

def repl():
	while True:
		user_input = input('Enter a message you would like to encode/decode:\n')
		print(decode(user_input))

		while True:
			play_again = input('Would you like to play again? ').lower().strip()
			if play_again in ['y', 'yes', 'n', 'no']:
				break

		if play_again.startswith('n'):
			break

repl()