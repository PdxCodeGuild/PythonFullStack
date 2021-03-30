





# mutable vs immutable =======================

# x = 5
# print(id(x))
# y = x
# print(id(y))
# y = y + 1
# print(id(y))
# print(x)
# print(y)


# x = ['a']
# print(id(x))
# y = x
# print(id(y))
# y.append('b')
# print(id(y))
# print(x)
# print(y)





# def swap(values, i, j):
#     values[i], values[j] = values[j], values[i]

# fruits = ['apples', 'bananas', 'pears']
# print(fruits)
# swap(fruits, 0, 1)
# print(fruits)


# def remove_all_tens(nums):
#     while 10 in nums:
#         nums.remove(10)
# nums = [5, 10, 15, 2, 3, 10, 3]
# remove_all_tens(nums)
# print(nums)


# def remove_all_tens(nums):
#     nums = nums.copy()
#     while 10 in nums:
#         nums.remove(10)
#     return nums
# original_nums = [5, 10, 15, 2, 3, 10, 3]
# new_nums = remove_all_tens(nums)
# print(new_nums)




# identity vs equality =============================

# '==' tests for equality
# 'is' tests for identity

# import random

# def check_x():
#     y = 5
#     print(id(y))

# def check_y():
#     x = 4
#     print(id(x))
#     x = x + 1
#     print(id(x))

# check_x()
# check_y()



# x = 'hello'
# y = 'hell'
# y += 'o'
# print(x)
# print(y)
# print(id(x))
# print(id(y))
# print(x == y)
# print(x is y) # print(id(x) == id(y))


# def say_hello():
#     print('hello world!')

# value = say_hello()
# if value == None:
#     print('value equals none')
# if value is None: # proper way
#     print('value is none')



# s = 'hello'
# s = s[:1] + s[2:]
# print(s)

# fruits = {'apples': 1, 'bananas': 2, 'cherries': 3}
# del fruits['apples']
# print(fruits)

