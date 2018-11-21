some_list = [1,2,3,4,5]

# some_list[1] += 10

for item in some_list:
    # item is a thing in this list
    thing = item


# use this type of for loop if you want to change the list
# or if you want to do something with the indexes
for i in range(len(some_list)): 
    # i is the index of the list
    thing = some_list[i]
    some_list[i] += 10 # making change in list

print(some_list)