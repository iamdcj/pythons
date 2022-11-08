# AND
a = True
b = True

if a and b:
    print(f"both are true")

## both are true

a = 0
b = 1

if a and b:
    print(f"both are true")
else: 
    print(f"a is false so we stop there")


a = True
b = True

if a or b:
    print(f"a is true so we stop")

## OR
a = 0
b = 1

if a or b:
    print(f"b is true so we stop")

b = 0

if a or b:
    print(f"a is true so we stop")
else:
    print("both a and b were false")
