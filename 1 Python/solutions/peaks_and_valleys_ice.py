# peaks_and_valleys_ice.py
def peaks(data):
	""" returns location of peaks in data
	"""
	peaks = []
	# print(len(data))
	for i in range(1, len(data)-1):
		# print(i-1, i, i+1)
		left = data[i-1]
		mid = data[i]
		right = data[i+1]
		if mid > right and mid > left:
			peaks.append(i)
	return peaks

def valleys(data):
	""" returns location of valleys in data
	"""
	valleys = []
	for i in range(1, len(data)-1):
		left = data[i-1]
		mid = data[i]
		right = data[i+1]
		if mid < right and mid < left:
			valleys.append(i)
	return valleys

def peaks_and_valleys(data):
	""" returns location of peaks and valleys sorted
	"""
	p = peaks(data)
	v = valleys(data)
	peaks_and_valleys = p + v # join peaks and valleys and sort them
	# peaks_and_valleys = p.extend(v) # equivalent to above

	return sorted(peaks_and_valleys) # -> returns a sorted copy of list
	# # equivalent to above
	# peaks_and_valleys.sort() # -> returns None
	# return peaks_and_valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
print(peaks(data))
print(valleys(data))
print(peaks_and_valleys(data))c