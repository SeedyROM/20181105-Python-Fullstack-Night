def avg(*args):
	sum = 0
	if len(args) == 0:
		return 0
	for arg in args:
		sum += arg
	return sum / len(args)


nums = []
print("Enter the numbers you want to average. Enter 'done' to calculate.")

while True:
	while True:
		try:
			user_input = input('Enter a number: ').strip().lower()
			user_input = int(user_input)
			break
		except ValueError:
			if user_input == 'done':
				break
			print("Enter a number or 'done'")

	if user_input == 'done':
		break
	nums.append(int(user_input))

print(avg(*nums))

