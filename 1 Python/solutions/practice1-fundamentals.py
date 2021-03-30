

# Problem 1
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)


# 5%2 == 1
# 17%2 == 1
# 16%2 == 0
def is_even(a):

    return a%2 == 0

    # return True if a%2 == 0 else False

    # if a % 2 == 0:
    #     return True
    # return False

    # if a % 2 == 0:
    #     return True
    # else:
    #     return False

# print(is_even(5)) # False
# print(is_even(6)) # True


# Problem 2
# Write a function that takes two integers, a and b, and returns True if one is positive and the other is negative, and return False otherwise.

def opposite(a, b):

    return a*b < 0

    # return (a > 0 and b < 0) or (a < 0 and b > 0)

    # if (a > 0 and b < 0) or (a < 0 and b > 0):
    #     return True
    # return False

    # if a > 0 and b < 0:
    #     return True
    # elif a < 0 and b > 0:
    #     return True
    # else:
    #     return False

# print(opposite(10, -1)) # True
# print(opposite(-10, 1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False




# Problem 3
# Write a function that returns True if a number within 10 of 100.

def near_100(num):

    # return abs(100-num) < 10
    
    # return True if 90 < num < 110 else False

    if 90 < num < 110: # if 90 < num and 110 > num:
        return True
    else:
        return False
    
# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True
# print(near_100(120)) # False



# Problem 4
# Write a function that returns the maximum of 3 parameters.



# nums = [5, 89, 35]

# nums.sort()
# print(nums[-1])

# nums.sort(reverse=True) # sort in descending order
# print(nums[0])

# nums.sort() # sort in ascending order
# nums.reverse() # reverse the list
# print(nums[0])

# print(nums)



def maximum_of_three(a, b, c):
    # nums = [a, b, c]
    # nums.sort(reverse=True)
    # return nums[0]

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

    # nums = [a, b, c]
    # big = a
    # for i in range(len(nums)):
    #     if big < nums[i]:
    #         big = nums[i]
    # return big
    

# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10
# print(maximum_of_three(-4,-3,-10)) # 10




# def max(nums):
#     running_maximum = nums[0]
#     for num in nums:
#         if num > running_maximum:
#             running_maximum = num
#     return running_maximum

# import random
# nums = []
# for i in range(100):
#     nums.append(random.randint(0, 100))
# print(nums)
# print(max(nums))





#             0         1         2
# fruits = ['apples', 'bananas', 'pears']
# # iterate over the indices, use the index to access the element
# for i in range(len(fruits)):
#     print(i, fruits[i])
# # iterate over the elements
# for fruit in fruits:
#     print(fruit)


# Problem 5
# Write a loop to print the powers of 2 from 2^0 to 2^20

# def print_powers_2():
#     for i in range(0, 20):
#         print(f'2^{i} =', 2 ** i)
# print_powers_2() # 1, 2, 4, 8, 16, 32, 64, ...


