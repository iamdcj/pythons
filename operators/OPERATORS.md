# Operators

Python has a number of operators that allow programmers to perform all kinds of operations within their programs


## Operator Precedence
Operator precedence in the python language is consistent with mathematics:

```
print((1+4) * 1 * 3)

```

In the above example the operations within the brackets takes precedence over the multiplication outside of the brackets, as per regular math.

## Comparison

Comparsion operators allow programmers to compare values, usually when dealing with control flow in an application.


Python _does not_ have a strict equality operator as per javascript, but if you compare two distinct types then the evaluation will return `false`

```
print([] == False)

## False

print('1' == 1)

## False
```

However, the integers `0` and `1` are cast to booleans when compared to booleans:

```
print(1 == True)

# True 

print(0 == False)

# True

```

### is

Comparsions can be performed using the `is` operator, however, this will return false for all non-primitive types:


```
print({} is {})  # False
print([1, 2, 3] is [1, 2, 3])  # False

```