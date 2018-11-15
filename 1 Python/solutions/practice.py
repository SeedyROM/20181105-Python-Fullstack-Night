def is_even(a):
    """ returns if number is even
    """
    return a%2 == 0

def opposite(a, b):
    """ returns if a and b have opposite polarity
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

def combine(nums1, nums2):
    """ returns combined list of alternating items
    """
    combined = []
    for i in range(len(nums1)):
        combined.append(nums1[i])
        combined.append(nums2[i])
    return combined
    # while (len(nums1) > 0 and len(nums2) > 0):
    #     combined.append(nums1.pop(0))
    #     combined.append(nums2.pop(0))
    # return combined

def latest_letter(string):
    """ returns letter latest in the English alphabet
    """    
    last = string[0]
    for char in string:
        char = char.lower()
        if char.isalpha():
            if char > last:
                last = char
    if last.isalpha():
        return last 
    return ''

# print(is_even(1)) # False
# print(is_even(2)) # True
# print(opposite(1, -1)) # True
# print(opposite(-1, 0)) # True
# print(opposite(-1, -9)) # False
# print(opposite(2, 3)) # False
# print(combine([1,2,3], [4,5,6])) # [1, 4, 2, 5, 3, 6]
print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
print(latest_letter('123')) # ''