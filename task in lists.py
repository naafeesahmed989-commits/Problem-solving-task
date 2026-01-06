# we should remove the duplicate in the list
numbers=[1,1,3,4,5,5,6]
# i will create a new list so i can store the item in it
numbers2=[]
# using for loop to move through items
for item in numbers:
    # a condition to check if we already have this num or not
    if item not in numbers2:
        # if not then add it to the list
        numbers2.append(item)
print(numbers2)


