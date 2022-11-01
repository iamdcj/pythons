# str

The `st` datatype represent a string in the python language.


Strings in Python are immutable, that is they cannot be modified once they are declared

```
stringy = "Dave"

stringy[2] = "n

### TypeError: 'str' object does not support item assignment

```

However, variables containing strings can be reassigned with a new string

```
stringy = "Dave"
stringy = "Dane" 

print(stringy) ## Dane
```

## Single-line strings

If you want to create a string on a single line this can be done simply by adding quotes around the string:

```
'David'
```

## Multi-line strings

If you require to break a string over multiple lines this can be achieved by adding three quotation marks at the start and end of the desired string

```
'''
David
Jones
'''
```

## Concatenation

Strings can be joined by using the `+` operator

```
print("David" + "Jones") ## DavidJones

```

## Conversion

Other value types an be converted to strings using the `str()` method

```
print(type(str(35))) ## <class 'str'>

```

## Escape Sequence

Python allows you to escape certain characters when creating strings:

```
print("My name isn\'t Joe")  ## My name isn't Joe


print("B-b-b-b-b-b-Backslash \\")  ## B-b-b-b-b-b-Backslash \

print("Line \n Break")

## Line
##  Break
```

## Formatting

You can parse variables within a string by passing the `f` flag at the start of the string sequence:

Python 3

```
name = "David"
age = 35
print(f'Hi, my name is {name}. I am {age} years old')

## Hi, my name is David. I am 35 years old
```

Python 2

```
print('Hi, my name is {0}. I am {1} years old'.format(name, age))

## Hi, my name is David. I am 35 years old
```


## Slicing
Python allows you to target elements within a string by essentially presenting them as individual items in a list, indexed at 0.


**Get element at index**
```
stringy = "0123456789"

print(string[0]) ## 0

```

**Get range of elements | start:end**

```
stringy = "0123456789"

print(string[0:3]) ## 012

```


**Step over elements | start:end:stepover**
This will grab every nth character in the list - in this case it will start at 0 and return every 3rd letter in the string, starting at 0 and ending at 10

```
stringy = "0123456789"

print(string[0:10:3]) ## 0369

```


**Flip string**
```
stringy = "0123456789"

print(stringy[::-1]) ## 9876543210

```