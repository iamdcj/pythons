if 2 > 1:
    print("greater than")

if 2 < 4:
    print("less than")

if 1 == True:
    print("equal to")

if 1 >= 0:
    print("greater than or equal to")

if 1 <= 2:
    print("less than or equal to")

if 1 != 2:
    print("does not equal")

## Truthy vs Falsy comparisons
print(10 == 10.0)  # True
print(10 == "10")  # False
print(1 == True)  # True
print(0 == False)  # True
print("1" == True)  # false
print([] == False)  # false
print([1, 2, 3] == [1, 2, 3])  # true

# Using IS
print(10 is 10.0)  # False
print(10 is "10")  # False
print(1 is True)  # False
print(0 is False)  # False
print("1" is True)  # False
print([] is False)  # False
print([1, 2, 3] is [1, 2, 3])  # False
