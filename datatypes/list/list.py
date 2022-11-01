intList = [1, 2, 3, 4, 5]
textList = ["a", "b", "c"]
mixedList = [1, True, "David", 1.5]

print(mixedList[0:2]) ## [1, True]

## mutate list

mixedList[0] = 2

print(mixedList) ## [2, True, 'David', 1.5]

newMixedList = mixedList

newMixedList[0] = "reference"

print(newMixedList) ## ['reference', True, 'David', 1.5]
print(mixedList) ## ['reference', True, 'David', 1.5]

## slice into new variable without affecting original
updatedMixedList = mixedList[:]

updatedMixedList[0] = 3

print(updatedMixedList) # [3, True, 'David', 1.5]
print(mixedList) # ['reference', True, 'David', 1.5]