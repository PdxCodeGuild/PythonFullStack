



# passing a function as a parameter to another function ===========

# def double(num):
#     return num * 2

# def square(num):
#     return num * num

# def operate(nums, func):
#     for i in range(len(nums)):
#         nums[i] = func(nums[i])

# nums = [1, 2, 3, 4]
# operate(nums, square)
# print(nums)


# renaming a function ===================

# p = print
# p('hello ' * 3)


# functions are objects ==================

# print(print)



# positional arguments ======================

# def add(a, b):
#     return a + b

# print(add(5)) # crash
# print(add(5, 1)) # okay
# print(add(5, 1, 2)) # crash


# optional/keyword arguments ======================

def add(a, b=1):
    return a + b

print(add(5))
print(add(5, 2))
print(add(5, b=6))

# print('hello', 'world', sep='_', end='!')


# args and kwargs ==============================

# args - able to pass a list as parameters

# def sum(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(sum([4, 5, 6, 7]))

# people = [('mike', 45), ('bob', 34), ('jill', 54)]

# def sum(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(sum(5, 6, 7, 8, 9, 10, 11, 12))



# def print(*args, sep=' ', end='\n'):



# def checkout(**cart):
#     print(cart)
#     total = 0
#     for item in cart:
#         total += cart[item]
#     return total
# print(checkout(apples=2, bananas=3, cherries=1.5))
# print(checkout({'apples': 2, 'bananas': 3, 'cherries': 1.5}))





# def get_name(names):
#     name = input('what is your name? ')
#     names.append(name)

# names = []
# for i in range(10):
#     get_name(names)
# print(names)




