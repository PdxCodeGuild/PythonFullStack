

# Problem 1
# Write a function that returns True if the given dictionary has the given key, False otherwise.

def has_key(d, key):
    if key in d:
        return True
    else:
        return False
# print(has_key({'a': 1, 'b': 2}, 'a')) # True
# print(has_key({'a': 1, 'b': 2}, 'c')) # False


# Problem 2
# Write a function that returns True if the given dictionary is empty, False otherwise.


# iterables - anything you can use on the right side of a for-loop
# e.g. strings, lists, tuples, range, dictionary

def is_empty(d):
    # return len(d) == 0
    return d == {}
    # if len(d) == 0:
    #     return True
    # return False
    

# print(is_empty({})) # True
# print(is_empty({'a': 1, 'b': 2})) # False


# a = range(10)
# b = range(10)
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# a = {}
# b = {}
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)

# class MyClass:
#     pass
# a = MyClass()
# b = MyClass()
# print(id(a))
# print(id(b))
# print(a == b)
# print(a is b)


# Problem 3
# Write a function that finds and returns the key for the given value, if the value is not in the dictionary, it should return None.

def find_key(d, value_to_find):
    # for k in d:
    #     if d[k] == value_to_find:
    #         return k
    for key, value in d.items():
        if value == value_to_find:
            return key
    return None

# print(find_key({'a': 1, 'b': 2}, 1)) # a
# print(find_key({'a': 1, 'b': 2}, 3)) # None


# Problem 4
# Write a function that takes a dictionary and returns a new dictionary with the keys and values reversed.

def reverse_dict(d):
    output = {}
    for key in d:
        value = d[key]
        output[value] = key
    return output
print(reverse_dict({'a': 1, 'b': 2})) # {1: 'a', 2: 'b'}




