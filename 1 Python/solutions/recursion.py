# recursion.py
from datetime import datetime


def factorial(n):
	"""
	factorial(n) = n * factorial(n-1)

	>>> factorial(5)
	120
	"""
	if n == 1:
		return 1
	return n * factorial(n-1) # recursive case


def fibonacci(n):
	"""
	fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

	>>> fibonacci(7)
	13
	"""
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci(n-1) + fibonacci(n-2)


cached_fibonacci = [0,1]
def memoized_fibonacci(n):
	"""
	fibonacci with memoization

	>>> memoized_fibonacci(100)
	354224848179261915075
	"""
	global cached_fibonacci
	if n < len(cached_fibonacci):
		return cached_fibonacci[n]
	fib_n = memoized_fibonacci(n-1) + memoized_fibonacci(n-2)
	cached_fibonacci.append(fib_n)
	return fib_n


def binary_search(l, target, start, end):
	"""
	l: list
	target: num or word
	start: start idx
	end: end idx
	searches sorted list l for target

	>>> binary_search([1,2,3,4,5,6,7], 7, 0, 7)
	6
	"""
	if start >= end: # target not in list
		return None
	mid = (end + start ) // 2
	if l[mid] == target: # target found
		return mid 
	if l[mid] < target: # search in right half
		return binary_search(l, target, mid+1, end)
	else: # l[mid] > target, search in left half
		return binary_search(l, target, start, mid)


if __name__ == '__main__':
	n = input('n: ')
	start = datetime.now()
	# fib_n = fibonacci(int(n))
	n = int(n)
	for i in range(n):
		fib_n = memoized_fibonacci(n)
	print(fib_n)
	print(f'Completed calculating {n} fibonacci numbers in {datetime.now() - start} sec')

