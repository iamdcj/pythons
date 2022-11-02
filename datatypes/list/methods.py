from cmath import log


intList = [1, 2, 3, 4, 5]

print(len(intList))  # 5


# append item
intList.append(6)

print(intList)  # [1, 2, 3, 4, 5, 6]


# insert item
intList.insert(1, 1.5)

print(intList)  # [1, 1.5, 2, 3, 4, 5, 6]


# remove from end
intList.pop()

print(intList)  # [1, 1.5, 2, 3, 4, 5]

# remove from index
popped = intList.pop(1)  # returns removed value
print(popped)  # 1.5

print(intList)  # [1, 2, 3, 4, 5]


# remove by value
intList.remove(1)

print(intList)  # [2, 3, 4, 5]

# clear list
intList.clear()

print(intList)  # []
