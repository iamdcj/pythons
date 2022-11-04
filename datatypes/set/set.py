a = {
    '1': 'twat'
}

b = {3, 1}

print(type(a))  # dict
print(type(b))  # set


set1 = {1, 2, 3, 5, 8, 13}
set2 = {0, 8, 13, 21, 34}


# difference - returns the difference between two sets, as a new set
print(set2.difference(set1))  # {0, 34, 21}


# discard - removes the specified member of the set, modifies in place
set2.discard(0)

print(set2)  # {34, 21, 8, 13}

# intersection
# will remove any intersection members when comparing two sets
# returns an intersection set
print('INTERSECTION: ', set2.intersection(set1))  # INTERSECTION:  {8, 13}
print('INTERSECTION: ', set2 & set1)  # INTERSECTION:  {8, 13}


# union
# will join multiple sets and remove any duplicates
print('UNION: ', set2.union(set1))  # UNION:  {1, 34, 2, 3, 5, 8, 13, 21}
print('UNION: ', set2 | set1)  # UNION:  {1, 34, 2, 3, 5, 8, 13, 21}


setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5, 6}

# issubset
# is a set a subset of another set, i.e. all members of a set are present in another set
# returns a boolean
print('IS A SUBSET: ', setA.issubset(setB))  # IS A SUBSET:  True
print('IS A SUBSET: ', setB.issubset(setA))  # IS A SUBSET:  False


# issuperset
# is a set a superset of another set, i.e. it contains all the other set members and more
# returns a boolean
print('IS A SUPERSET: ', setA.issuperset(setB))  # IS A SUPERSET:  False
print('IS A SUPERSET: ', setB.issuperset(setA))  # IS A SUPERSET:  True


# difference_update - removes the difference between two sets,
# i.e. it removes any clashing members in the passed set,
# modifies in place
print('SET 1: ', set1)  # SET 1:  {1, 2, 3, 5, 8, 13}
print('ORIGINAL: ', set2)  # ORIGINAL:  {34, 21, 8, 13}


set2.difference_update(set1)

print('UPDATED: ', set2)  # UPDATED:  {34, 21}
