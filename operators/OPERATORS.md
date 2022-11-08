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
```