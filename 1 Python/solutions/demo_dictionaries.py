


# defining a dictionary
d = {'apple': 1.0, 'pear': 1.5, 'grapes': 0.75}


# you can use any immutable as the key (None, boolean, int, float, string, tuple)
# you can use anything for the value

# abomination = {
#     None: 5,
#     True: 6,
#     False: 7,
#     8: 8,
#     9.5: 9,
#     'print': print,
# }
# print(abomination[None]) # 5
# print(abomination[True]) # 6
# abomination['print']('hello!')



# using a key to access a value
print(d['apple']) # 1.0

# changing a value for a given key
d['apple'] = 1.25
print(d['apple']) # 1.25

# adding a new key-value pair
d['cherries'] = 5.0
print(d)

# if you try to use a key that doesn't exist in the dictionary it'll crash
# print(d['avocado']) # KeyError: 'avocado'

# the .get method will return the value for a key or None if the key isn't in the dictionary
print(d.get('avocado'))
# the .get method can also take a default value
print(d.get('avocado', 4.0))


del d['apple']
print(d)


if 'avocado' in d:
    print(d['avocado'])
else:
    print(None)


fruits = {'apple': 1.0, 'banana': 1.5, 'pear': 0.75}
fruits.update({'banana': 0.25})
print(fruits)



# from collections import OrderedDict
# d = OrderedDict({'a': 1, 'b': 2, 'c':3})
# print(d)


fruits = {'apple': 1.0, 'banana': 0.25, 'pear': 0.75}
for key in fruits:
    print(key, fruits[key])


print(fruits.keys())
print(fruits.values())
print(fruits.items())


# import string
# letters = {}
# for i in range(len(string.ascii_letters)):
#     letters[string.ascii_letters[i]] = i
# print(''.join(letters.keys()))

# names = ('john', 'james', 'jim')
# names = list(names)
# names.append('bob')
# names = tuple(names)
# print(names)

