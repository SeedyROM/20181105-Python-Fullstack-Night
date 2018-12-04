# comprehensions

# mapped_list = [variable for variable in a_list]
# filtered_list = [variable for variable in a_list 
#                           if variable == condition]
# nested_comprehension = [(x,y) for x in a_list 
#                               for y in another_list]

nums = [1,2,3,4,5,6,7,8,9,10]
nums_plus_one = [num + 1 for num in nums] # [2,3,4,5,6,7,8,9,10,11]
multiple_of_three = [num for num in nums 
                         if num % 3 == 0] # [3,6,9]

list_a = [1,2,3]
list_b = ['a', 'b']
nested_a_times_b = [(a, b) for a in list_a 
                           for b in list_b]
# [(1,a), (1,b), (2,a), (2,b), (3,a), (3,b)]

print(nums_plus_one)
print(multiple_of_three)
print(nested_a_times_b)