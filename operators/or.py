a = True
b = True

if a or b:
    print(f"a is true so we stop")

a = 0
b = 1

if a or b:
    print(f"b is true so we stop")

b = 0

if a or b:
    print(f"a is true so we stop")
else:
    print("both a and b were false")
