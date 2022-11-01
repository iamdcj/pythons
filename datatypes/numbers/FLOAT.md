# float

The `float` datatype represent a floating-point number in the python language.


```
someFloat = 3.14 

print(type(someFloat))

// <class 'float'>

```

All division operations will yield a `float`:

```
print(type(2 / 4))

// <class 'float'>
```

Unless you use the floor division operator (`//`) or the modulo operator(`%`):


```
print(type(2 // 4))

// <class 'int'>

print(type(2 % 4))

// <class 'int'>
```

All mathematical operations using floats will yield a float:

```
print(type(2.1 + 2.9))

// <class 'float'>
```