


# identity vs equality
# identity tests if two variables point to the same object
# equality tests if two variables have the same value

# x = 5
# y = x
# y += 1
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# print(x == y)
# print(x is y)



# types
# string, float, int, list, dictionary
# none, tuple, boolean, set, range

# iterables - types that can be used with a for-loop
# string, list, tuple, dictionary, range, dict_keys, dict_values, dict_items, reverse()
# you can turn any iterable into a list using list(x)


# d = {'a': 1, 'b': 2}
# print(list(d.keys()))

# nums = [1, 2, 3]
# print(reversed(nums))
# for num in reversed(nums):
#     print(num) # 3, 2, 1

# for num in sorted(nums):
#     print(num) # 1, 2, 3

# x = range(10)
# print(x)
# print(type(x))

# import requests
# response = requests.get('https://www.google.com/')
# print(type(response))




# range(10) # 0 - 9
# range(5, 16) # 5 - 15
# range(10, 21, 2) # 10, 12, 14, 16, 18, 20
# range(19, 5, -3) # 19, 16, 13, 10, 7

#      0123456789...
# s = 'helloworld123abcllama'
# s[4] # o
# s[2:7] # llowo
# s[0:10:2] # hlowrd
# s[5:] # world123abcllama
# s[:5] # hello


# continue goes back up to the top
# break ends the loop


# fruits = ['apples', 'bananas', 'pears']
# fruits = fruits.append('kiwi') # fruits will be none after this
# fruits.append('kiwi')
# fruits2 = fruits.copy()
# print(fruits)

# text = 'Mr Bill'
# text = text.lower()
# print(text) # 'Mr Bill'


# import random
# def shuffle(nums):
#     nums = nums.copy()
#     for i in range(len(nums)):
#         j = random.randint(0, len(nums)-1)
#         nums[i], nums[j] = nums[j], nums[i]
#     return nums
# nums = [1, 2, 3, 4]
# nums = shuffle(nums)
# print(nums)





# x = print('hello world')
# print(x) # None
# print(print('hello world')) # None



# for i in range(100):
#     print(i, end=' ')
# print()


# print('hello', end=' ')
# print('world')

# print(5, 6, 2, 3)
# print(5, 6, 2, 3, sep=' ')
# print(5, 6, 2, 3, sep='_')


# x = 5
# y = 'hello'
# x = int()




# print(16%5) # 1
# print(876%2) # 0
# print(99%6) # 3

# fruits = ['apples', 'bananas', 'pears']
# for i in range(100):
#     print(fruits[i%len(fruits)])


# import random
# random.randint - returns a random integer between a lower and upper bound
# random.choice - takes any iterable, returns a random element
# random.shuffle - takes a list and shuffles it in-place

# import random
# for i in range(10):
#     print(random.random())

# def randint(lower, upper):
#     return int(lower + random.random()*(upper-lower))


text = 'hello world'
text = text.replace('world', 'earth')
text = text.title()
print(text)







# short-circuited evaluation
# if you have two conditions on either side of an 'and' and the first is false, it won't check the second
# if you have two conditions on either side of an 'or' and the second 


# def is_sorted(nums):

#     # for i in range(len(nums)):
#     #     if nums[i] > nums[i+1]:
#     #         return False
#     # return True

#     # for i in range(len(nums)-1):
#     #     if nums[i] > nums[i+1]:
#     #         return False
#     # return True

#     for i in range(len(nums)):
#         if i < len(nums)-1 and nums[i] > nums[i+1]:
#             return False
#     return True


# nums = [1, 2, 3, 4]
# print(is_sorted(nums))



# x = 5
# y = 7
# print(x == y) # false
# print(x is y) # false




# all values are truthy except
# None, 0, '', [], {}


# keep_playing = False
# if keep_playing: # fine



# x = 5
# if x != 0:
#     print('x is not 0')

# values = [0, 1, '', 'hi', [], ['hi'], {}, {'a':1}]
# for value in values:
#     print(value, 'is', end=' ')
#     if value:
#         print('truthy')
#     else:
#         print('falsey')


# x = int(input('enter a positive integer: '))
# x = -x if x < 0 else x
# x = math.abs(x)





# Problem 1
# Write a comprehension to generate the first 10 powers of two.
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]


nums = [2**i for i in range(10)] # blank list we can append values to
print(nums)

# word = 'hello'
# underscores = ['_']*len(word)
# underscores = ['_' for i in range(len(word))]














# TODO - static properties and methods

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def distance(self, p):
#         ...

# p = Point(5, 2)
# p.x # 5
# p.distance(x)


