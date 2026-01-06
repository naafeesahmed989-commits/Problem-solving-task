# the task is to remove the duplicates in a list
numbers=[1,1,3,4,5,5,6]
# i will create a new list so i can store the items in it
numbers2=[]
# using for loop to move through items
for item in numbers:
    # a condition to check if we already have this num or not
    if item not in numbers2:
        # if it is not there then add it to the list
        numbers2.append(item)
print(numbers2)




