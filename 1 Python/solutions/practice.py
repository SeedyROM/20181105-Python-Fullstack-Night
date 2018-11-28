def is_even(a):
    """ returns if number is even

    >>> is_even(1)
    False
    >>> is_even(2)
    True
    """
    return a%2 == 0

def opposite(a, b):
    """ returns if a and b have opposite polarity
    
    >>> opposite(1, -1)
    True
    >>> opposite(-1, 0)
    True
    >>> opposite(-1, -9)
    False
    >>> opposite(2, 3)
    False
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

def combine_lists(list1, list2):
    """ 
    returns combined list of alternating items

    >>> combine_lists([1,2,3], [4,5,6])
    [1, 4, 2, 5, 3, 6]
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
    
    >>> latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')
    'v'
    >>> latest_letter('123')
    ''
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

    >>> max([2,4,-9000,7,11,0])
    11
    """
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num
    return running_max

def sum(nums):
    """ returns sum of list of numbers

    >>> sum([1,2,3,4,5])
    15
    """
    total = 0
    for num in nums:
        total += num
    return total

def eveneven(nums):
    """ returns true if there are an even amount of even numbers in nums

    >>> eveneven([5, 6, 2])
    True
    >>> eveneven([5, 5, 2])
    False
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
    
    >>> combine_lists_to_dict(['a', 'b', 'c'], ['apples', 'bananas', 'cherries'])
    {'a': 'apples', 'b': 'bananas', 'c': 'cherries'}
    """
    return dict(zip(keys, values))
    # # equivalent to above
    # combined = {}
    # for i in range(len(values)):
    #     combined[keys[i]] = values[i]
    # return combined

def squared(nums):
    """ returns list of nums squared

    >>> squared([1,2,3,4,5])
    [1, 4, 9, 16, 25]
    """
    return [num*num for num in nums]

def even_squares(nums):
    """ returns square of num if num is even
    
    >>> even_squares([1,2,3,4,5])
    [4, 16]
    """    
    return [num*num for num in nums if num % 2 == 0]

def average(d):
    """
    return average of values in d

    >>> average({'apple':1.2, 'banana':3.3, 'pear':2.1})
    2.1999999999999997
    """
    # total_sum = 0
    # for k in d:
    #     total_sum += d[k]
    # return total_sum / len(d)

    return sum(d.values()) / len(d)    

def minimum(nums):
    """
    returns min of list of nums
    >>> minimum([2,-1,11,8,6])
    -1
    """
    # return min(nums)
    running_min = float('inf')
    for num in nums:
        if num < running_min:
            running_min = num 
    return running_min

def maximum(nums):
    """
    returns max of list of nums
    >>> maximum([2,-1,11,400,-2222])
    400
    """
    # return max(nums)
    running_max = float('-inf')
    for num in nums:
        if num > running_max:
            running_max = num 
    return running_max

def mean(nums):
    """
    returns avg of list of nums
    >>> mean([2,2,2,2,2])
    2.0
    """
    return sum(nums)/len(nums)

def mode(nums): # (OPTIONAL)
    """
    returns mode of list of nums
    >>> mode([2,-1,11,2,11,1])
    [2, 11]
    """
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    sorted_count = sorted(count.items(), key=lambda kv: kv[1], reverse=True)
    max_count = sorted_count[0][0]
    mode = []
    for item in sorted_count:
        if item[1] == max_count:
            mode.append(item[0])
        else:
            break
    return mode