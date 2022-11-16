i = 0

while i < 5:
    i += 1
    if i == 3:
        break
    else:
        print(i)


x = 0

while x < 5:
    print("before continue", x)
    x += 1
    continue
    print(x)

# before continue 0
# before continue 1
# before continue 2
# before continue 3
# before continue 4
