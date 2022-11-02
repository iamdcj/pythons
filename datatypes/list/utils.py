# easily generate a numbered list
print(list(range(1,10)))


# joining list of strings
listy = ' '.join(['I','am','David','Jones'])

print(listy) # I am David Jones


# unpacking
a,b,c, *rest, f = ["a", "b", "c", "d", "e", "f"]

print(a, b, c)  # a b c
print(rest) # ['d', 'e', 'f']
print(f) # f