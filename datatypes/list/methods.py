from cmath import log


intList = [1, 2, 3, 4, 5]

# returns length of list
print(len(intList))  # 5


# append item - returns None, modifies in place
intList.append(6)

print(intList)  # [1, 2, 3, 4, 5, 6]


# insert item - returns None, modifies in place
intList.insert(1, 1.5)

print(intList)  # [1, 1.5, 2, 3, 4, 5, 6]


# remove from end - returns None, modifies in place
intList.pop()

print(intList)  # [1, 1.5, 2, 3, 4, 5]

# remove from index - returns removed value
popped = intList.pop(1)  
print(popped)  # 1.5

print(intList)  # [1, 2, 3, 4, 5]


# remove by value - returns None, modifies in place
intList.remove(1)

print(intList)  # [2, 3, 4, 5]

# clear list - clears entire list
intList.clear()

print(intList)  # []



stringList = ['David', 'Steffie', 'Steffie', 'Nolé']

# index - returns index of the item, if item is found in list
print(stringList.index('Steffie'))  # 1


# count - returns an integer reflecting how many times an item is within a list
print(stringList.count('Steffie')) # 2


# sort - sorts list (default: alphabetically) - returns None, modifies in place
stringList.sort()
print(stringList) # ['David', 'Nolé', 'Steffie', 'Steffie']


# copy - copies list - returns new array
copiedList = stringList.copy()
print('COPY: ', copiedList)
print('ORIGINAL: ', stringList)

# reverse - reverses list - returns None, modifies in place
reversed = stringList.reverse()
print('REVERSE: ', stringList)



