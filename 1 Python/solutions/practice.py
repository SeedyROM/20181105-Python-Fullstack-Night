def is_even(a):
    """ returns if number is even
    """
    return a%2 == 0

def opposite(a, b):
    """ returns if a and b have opposite polarity
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

def combine_lists(list1, list2):
    """ returns combined list of alternating items
    """
    combined = []
    for i in range(len(list1)):
        combined.append(list1[i])
        combined.append(list2[i])
    return combined
    # while (len(list1) > 0 and len(list2) > 0):
    #     combined.append(list1.pop(0))
    #     combined.append(list2.pop(0))
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

def max(nums):
    """ returns max of list of numbers
    """
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max

def sum(nums):
    """ returns sum of list of numbers
    """
    total = 0
    for num in nums:
        total += num
    return total

def eveneven(nums):
    """ returns true if there are an even amount of even numbers in nums
    """
    even_nums = [num for num in nums if num % 2 == 0]
    # # equivalent to above
    # even_nums = []
    # for num in nums:
    #     if num % 2 == 0:
    #         even_nums.append(num)

    return len(even_nums) % 2 == 0


def combine_lists_to_dict(keys, values):
    """ returns dict of keys zipped to values
    """
    return dict(zip(keys, values))
    # # equivalent to above
    # combined = {}
    # for i in range(len(values)):
    #     combined[keys[i]] = values[i]
    # return combined

def squared(nums):
    """ returns list of nums squared
    """
    return [num*num for num in nums]

def even_squares(nums):
    """ returns square of num if num is even
    """    
    return [num*num for num in nums if num % 2 == 0]

# print(is_even(1)) # False
# print(is_even(2)) # True
# print(opposite(1, -1)) # True
# print(opposite(-1, 0)) # True
# print(opposite(-1, -9)) # False
# print(opposite(2, 3)) # False
# print(combine_lists([1,2,3], [4,5,6])) # [1, 4, 2, 5, 3, 6]
# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v
# print(latest_letter('123')) # ''
# print(max([2,4,-9000,7,11,0]))
# print(sum([1,2,3,4,5]))
print(eveneven([5, 6, 2])) # → True
print(eveneven([5, 5, 2])) # → False
key_list = ['a', 'b', 'c']
val_list = ['apples', 'bananas', 'cherries']
print(combine_lists_to_dict(key_list, val_list)) # {'a': 'apples', 'b': 'bananas', 'c': 'cherries'}

print(squared([1,2,3,4,5]))
print(even_squares([1,2,3,4,5]))