# bool

The `bool` datatype represent a boolean in the python language.

```
someBool = True
```

## Casting

Values can be explictly cast to a boolean via the `bool()` method:

```
isTruthy = 1
isFalsy = 0

print(bool(isTruthy))

## True

isFalsy = 0

 print(bool(isFalsy))

## False
```

### Implicit casting: truthy / falsy

As per other languages python will cast certain datatypes to a boolean based on value. e.g.

```
isTruthy = 1
isFalsy = 0


if isTruthy:
    print(bool(isTruthy))
    print('this is a truthy value')

# True
# this is a truthy value
```

In the above example the compiler casts the value of `isTruthy` to boolean, in this case it is cast to `True`

```
isTruthy = 1
isFalsy = 0


if not isFalsy:
    print(Bool(isFalsy))
    print('this is a falsy value')

# False
# this is a falsy value
```

In the above example the compiler casts the value of `isFalsy` to boolean, in this case it is cast to `False`
