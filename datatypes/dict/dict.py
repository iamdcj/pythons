someDict = {
    'a': [1,2,3],
    'b': False,
    'c': "HOLA",
    'd': {
        'a': 'HEY'
    }
}

print(someDict['a'][1]) # 2
print(someDict['b']) # False
print(someDict['c']) # HOLA
print(someDict['d']['a']) # HEY


## Clashing Keys
someDict = {
    'a': [1,2,3],
    'b': False,
    'c': "HOLA",
    'c': "Hello"
}

print(someDict['c']) # Hello