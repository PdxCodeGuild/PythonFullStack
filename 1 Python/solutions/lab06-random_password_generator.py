



#    0123456789
s = 'helloworld'
for char in s:
    print(char)

for i in range(len(s)):
    print(s[i])

# x = list(range(10))
# print(x)

# 0, 1, 2, 3, ... 9
for i in range(10):
    print(i, end=' ')
print()

# 2, 3, ... 9
for i in range(2, 10):
    print(i, end=' ')
print()

# 2, 4, 6, 8, 10
for i in range(2, 12, 2):
    print(i, end=' ')
print()






# for i in range(len(s)):
#     print(i, s[i])


import random
import string
import helpers



alphabet = string.ascii_letters + string.digits + string.punctuation

n = helpers.get_integer('Enter the length of the password: ')
password = ''

# i = 0
# while i < n:
#     password += random.choice(alphabet)
#     i += 1

for i in range(n):
    password += random.choice(alphabet)


# split and join =================================

# import random
# letters = list('abcdefg')
# random.shuffle(letters)
# output = ''.join(letters)
# print(output)

# fruits = 'apples, bananas, pears, cherries'
# print(fruits)
# fruits = fruits.split(', ')
# print(fruits)
# # for i in range(len(fruits)):
# #     fruits[i] = fruits[i].strip()
# fruits = '_'.join(fruits)
# print(fruits)


# numbers = input('enter 3 numbers, separated by spaces: ')
# print(numbers)
# numbers = numbers.split(' ')
# print(numbers)
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
# print(numbers)








# working with tuples =========================================

# import random


# def get_size():
#     return 800, 600

# x, y = get_size()
# print(x)
# print(y)

# x, y = y, x

# print(x)
# print(y)




# def swap(i, j, values):
#     # t = values[i]
#     # values[i] = values[j]
#     # values[j] = t

#     values[i], values[j] = values[j], values[i]


# fruits = ['apples', 'bananas', 'pears']
# swap(0, 1, fruits)
# print(fruits)














# print(random.choice('abcdef'))
# print(random.choice({'a': 1, 'b': 2, 'c': 3}))





