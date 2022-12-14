for x in [1, 2]:
    for y in "David":
        print(x, y)
# 1 D
# 1 a
# 1 v
# 1 i
# 1 d
# 2 D
# 2 a
# 2 v
# 2 i
# 2 d

for x in "some string":
    print(x)

someList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for n in someList:
    counter += n

print(counter)

# 55

someDic = {
    0: "a",
    1: "b",
    2: "c",
}

for x in someDic:
    print(x)

# 0
# 1
# 2

for x in someDic.values():
    print(x)

# a
# b
# c

for x in someDic.items():
    print(x)

# (0, 'a')
# (1, 'b')
# (2, 'c')


aTuple = (1, 2, 3)

for x in aTuple:
    print(x)

# 1
# 2
# 3


setA = {1, 2, 3}

for x in setA:
    print(x)

# 1
# 2
# 3


for i in range(0, 10):
    print(i)

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


for i in range(0, 10, 2):
    print(i)

# 0
# 2
# 4
# 6
# 8


for i in range(10, 0, -1):
    print(i)

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

for i in range(1):
    print(list(range(10, 0, -1)))

# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


for i in enumerate('hey'):
    print(i)

# (0, 'h')
# (1, 'e')
# (2, 'y')

## allows index-based value accessing


for index, integer in enumerate(list(range(1, 5))):
    print(index, integer)

# (0, 1)
# (1, 2)
# (2, 3)
# (3, 4)

for index, integer in enumerate(list(range(1, 5))):
    print(f"index of 3 is {index}" if integer == 3 else "")
# index of 3 is 2