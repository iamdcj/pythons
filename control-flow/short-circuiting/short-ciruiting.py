x = 3
y = 2
b = 1

if x > y or y < b:
    print('oi oi')


result = x or y

print(result)


x = 0

result = x and y

print(result)


if 1 and 0:
    print("'both the same")