# The 'for' statement

This allows engineers to iterate over any explicit iterable in the language, item-by-item.

## Lists

```
for x in [1,2,3,4]:
    print(x)

# 1
# 2
# 3
# 4
```

## Dictionaries

If you iterate over a dictonary the keys will be used as the value on each iteration:

```
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
```

However, the values can easily be return by targeting the values:

```
for x in someDic.values():
    print(x)

# a
# b
# c
```

And if you want both the key and the value of each item you can grab them using `.items()` - this will return a tuple for each key-value pair in the dictonary

```
for x in someDic.items():
    print(x)

# (0, 'a')
# (1, 'b')
# (2, 'c')
```

If you want to separate the key and value pairs returned from `.items()` you can unpack each item thus:

```
for key, value in someDic.items():
    print(key, value)

# 0, a
# 1, b
# 2, c
```

## Tuples

## Sets

## Strings
