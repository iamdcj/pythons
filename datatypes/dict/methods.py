someDict = {
    'a': [1,2,3],
    'b': False,
    'c': "HOLA",
    'd': {
        'a': 'HEY'
    }
}


# get
print(someDict.get('a')) # [1,2,3]
print(someDict.get('y')) # None

# get - default value
print(someDict.get('y', 'HEY')) # HEY


# values
print(someDict.values())  # dict_values([[1, 2, 3], False, 'HOLA', {'a': 'HEY'}])
print('HOLA' in someDict.values())  # True


# keys
print(someDict.keys())  # dict_keys(['a', 'b', 'c', 'd'])
print('d' in someDict.keys())  # True


# items
print(someDict.items()) # dict_items([('a', [1, 2, 3]), ('b', False), ('c', 'HOLA'), ('d', {'a': 'HEY'})])


# copy - modifies in place, returns new object
dict2 = someDict.copy()
print(dict2) # {'a': [1, 2, 3], 'b': False, 'c': 'HOLA', 'd': {'a': 'HEY'}}


# clear - modifies in place, does not return a value
someDict.clear()
print(someDict) # {}


# pop - returns value of the removed key
print(dict2.pop('a')) # [1, 2, 3]
print(dict2) # {'b': False, 'c': 'HOLA', 'd': {'a': 'HEY'}}


# popitem - returns value of the randomly removed key
print(dict2.popitem()) # ('d', {'a': 'HEY'})
print(dict2) # {'b': False, 'c': 'HOLA'}


# update - updates value - does not return value
print(dict2.update({ 'b': True })) # None
print(dict2.update({ 'g': 'man' })) # None
print(dict2) # {'b': True, 'c': 'HOLA', 'g': 'man'}