

import random

# Problem 1
# Write a function using random.randint to generate an random index, use that index to pick an element of a list and return it.


def random_element(a):
    i = random.randint(0, len(a)-1)
    return a[i]
#                         0         1         2
# print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'
# print(random_element(['apples', 'bananas', 'pears', 'cherries']))


# i = 0
# while i < 10:
#     print(i)
#     i += 1

# iterables - range, string, list, tuple, dictionary, set

# for i in range(10):
#     print(i)

# #            0          1         2
# fruits = ['apples', 'bananas', 'pears']
# for fruit in fruits:
#     fruit += '!'
#     print(fruit)
# print(fruits)

# for i in range(len(fruits)):
#     print(i, fruits[i])
#     fruits[i] += '!'
# print(fruits)

# Problem 2
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

def eveneven(nums):
    # step 1 - create an empty output list
    output = []
    # step 2 - iterate over input list
    for i in range(len(nums)):
        # step 3 - check if a given element from the input list is even
        if nums[i] % 2 == 0:
            # step 4 - if it's even, append the element to the output list
            output.append(nums[i])
            # step 5 - if it's odd, keep it where it is
    # step 6 - if the list length % 2 gives us a remainder of 0, return true, otherwise return false
    if len(output) % 2 == 0:
        return True
    return False

# def eveneven(nums):
#     output = 0
#     for num in nums:
#         if num%2 == 0:
#             output += 1
#     return output%2 == 0

# print(eveneven([5, 6, 2])) # True
# print(eveneven([5, 5, 2])) # False


# Problem 3
# Write a function that returns the reverse of a list.

# for i in range(10, 0, -1):
#     print(i)


def reverse(nums):

    output = nums.copy()
    output.reverse()
    return output

    # count = len(nums) - 1
    # output = []
    # while count >= 0:
    #     output.append(nums[count])
    #     count -= 1
    # return output

    # output = []
    # for i in range(len(nums)-1, -1, -1):
    #     print(i)
    #     output.append(nums[i])
    # return output

    # output = []
    # for i in range(len(nums)):
    #     # print(i, len(nums)-i-1)
    #     output.append(nums[len(nums)-i-1])
    # return output

    # output = []
    # r = list(range(len(nums)))
    # r.reverse()
    # print(r)
    # for i in r:
    #     output.append(nums[i])
    # return output

    # output = []
    # for num in nums:
    #     output.insert(0, num)
    # return output

    # output = []
    # while len(nums) > 0:
    #     output.append(nums.pop())
    # return output

# print(reverse(['a', 'b', 'c', 'd', 'e', 'f']))


# Problem 4
# Write a function to copy all the elements of a list with value less than 10 to a new list and return it.

def extract_less_than_ten(nums):
    new_values = []  # start with an empty list
    for num in nums:  # iterate over each number in our list
        if num < 10:  # if the number is less than 10
            new_values.append(num)  # add it to our new list
    return new_values
# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]
# print(extract_less_than_ten([5, 12, 3, 17, 9, 8, 34])) # [5, 3, 9, 8]


# Problem 5
# Write a function to find all common elements between two lists.

def common_elements(nums1, nums2):
    # step 1 - create an empty output list
    output = []
    # step 2 - iterate over the first list
    for i in range(len(nums1)):
        # step 3 - iterate over the second list
        for j in range(len(nums2)):
            # step 4 - compare values from each
            if nums1[i] == nums2[j]:
                # step 5 - if they're equal, add them to the output list
                output.append(nums2[j])
    # step 6 - return our output list
    return output

    # output = []
    # for num in nums1:
    #     if num in nums2:
    #         output.append(num)
    # return output

    # return list(set(nums1) & set(nums2))

# print(common_elements([1, 2, 2, 3], [2, 3, 4])) # [2, 3]


# matrix visualization
# https://docs.google.com/spreadsheets/d/1Qnije7G1O_AvXHsh1EtRC8EiALd7T4DmHVjYasVKV6A/edit?usp=sharing

def advent_problem1(nums):

    # if a + b == 2020
    #     return a * b

    # the problem with this one - adding a number to itself
    # [5, 6, 2, 3] -> 5+5, 6+6
    # for num1 in nums:
    #     for num2 in nums:
    #         if num1 + num2 == 2020:
    #             print(str(num1) + '+' + str(num2))

    # the problem with this one - you could have the same number twice
    # [5, 6, 5, 3] -> you wouldn't test 5+5
    # for num1 in nums:
    #     for num2 in nums:
    #         if num1 != num2:
    #             if num1 + num2 == 2020:
    #                 return num1 * num2

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j and nums[i] + nums[j] == 2020:
    #             return nums[i] * nums[j]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i != j and nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


#        0     1    2    3    4     5
# nums = [1721, 979, 366, 299, 675, 1456]
# print(advent_problem1(nums)) # 514579
# nums = [1010, 800, 600, 1010, 200]
# print(advent_problem1(nums)) # 1020100

# nums = [1974, 1773, 1841, 1932, 1951, 1852, 2000, 1988, 1998, 1670, 969, 2008, 1713, 2007, 1916, 1286, 1652, 1821, 1730, 2002, 1761, 1656, 814, 1999, 2010, 1936, 1794, 1905, 1250, 1920, 1986, 1709, 1914, 1681, 1820, 1982, 1961, 1931, 1331, 1923, 1972, 1631, 1643, 1719, 1926, 1994, 1952, 1981, 1847, 1774, 1296, 1946, 873, 2005, 173, 2006, 1960, 1872, 1894, 1695, 1769, 1800, 1734, 1675, 1860, 1383, 1947, 1768, 1827, 1877, 1721, 1738, 384, 1996, 1958, 1909, 1639, 1831, 1212, 1627, 1699, 1661, 1653, 1748, 1919, 1983, 1223, 1690, 1948, 1218, 1971, 1969, 1753, 1957, 1977, 1943, 1978, 1778, 1937, 1868, 1641, 1979, 1854, 1959, 1739, 2004, 1964, 760, 1890, 1701, 1940, 1840, 1817, 1966, 1799, 1941, 1934, 1929, 1962, 1691, 1927, 1764, 1945, 795, 1993, 1804, 1693, 1970, 1728, 1818, 1545, 1992, 1965, 1786, 2009, 1980, 1698, 1647, 1935, 1880, 1921, 1904, 1953, 1871, 1671, 1826, 1989, 1950, 1791, 1990, 1949, 1301, 1975, 1968, 1895, 1208, 1424, 1985, 1665, 1685, 1942, 1669, 64, 1832, 1995, 1987, 1955, 352, 1984, 1925, 1891, 1933, 1679, 2001, 1930, 1991, 1227, 1973, 1723, 1683, 132, 1718, 1944, 1908, 1900, 1657, 1954, 92, 1997, 1938, 1976, 1747, 1226, 1782, 1963, 1746, 1540, 1759, 1939, 1743]
# print(advent_problem1(nums))


# Problem 6
# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):

    # nums1 index 0
    # nums2 index 0
    # nums1 index 1
    # nums2 index 1
    # nums1 index 2
    # nums2 index 2

    combo = []
    for i in range(len(nums1)):
        # print(i, nums1[i], nums2[i])
        # combo += [nums1[i], nums2[i]]
        combo.append(nums1[i])
        combo.append(nums2[i])

    return combo

#   0   1   2
# ['a','b','c']
# [ 1,  2,  3 ]

# print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]


# Problem 7
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number.

# def find_pair(nums, target):
#     for num1 in nums:
#         for num2 in nums:
#             if num1 + num2 == target:
#                 return [num1, num2]
#                 # output = []
#                 # output.append(num1)
#                 # output.append(num2)
#                 # return output
# print(find_pair([5, 6, 2, 3], 7)) # [5, 2]

def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return None
# print(find_pair([5, 6, 2, 3], 7)) # [5, 2]
# print(find_pair([6, -2, 2, 3], 0)) # [-2, 2]


# Problem 8
# Write a function to find the average of a list of numbers

def average(nums):
    '''returns the average of a list'''
    # add up everything in nums to get a total
    # total = 0
    # total += nums[0]
    # total += nums[1]
    # total += nums[2]
    # ...

    # total = 0
    # for i in range(len(nums)):
    #     total += nums[i]
    # return total / len(nums)

    total = 0
    for num in nums:
        total += num
    return total / len(nums)

    # return sum(nums)/len(nums)

    # make an integer for the length of the list
    # divide the total by the length, return it

# print(average([1, 2, 3, 4, 5])) # 3
# print(average([56, 78, 12, 157])) # 3


# Problem 9
# Write a function to remove all empty strings from a list.

# def remove_empty(mylist)
#     ...
# print(remove_empty(['a', 'b', '', 'c', '', 'd'])) # ['a', 'b', 'c', 'd']


# if we're modifying a list as we're iterating over it
# be sure that we're not skipping over elements


# removing b's from the list

#   i
#   0    1    2    3
# ['a', 'b', 'b', 'c']

#        i
#   0    1    2    3
# ['a', 'b', 'b', 'c']

#             i
#   0    1    2
# ['a', 'b', 'c']


# mylist = ['a', 'b', 'b', 'c']

# bad code
# for i in range(len(mylist)):
#     if mylist[i] == 'b':
#         mylist.pop(i) # remove the element at index i

# good code
# i = 0
# while i < len(mylist):
#     if mylist[i] == 'b':
#         mylist.pop(i)
#     else:
#         i += 1


def remove_blanks(mylist):

    output = []
    for i in range(len(mylist)):
        if mylist[i] != '':
            output.append(mylist[i])
    return output

    # while '' in mylist:
    #     mylist.remove('')

    # for element in mylist:
    #     if element == character:
    #         mylist.remove(element)
    # return mylist
    # ['a', 'b', 'c', 'd']

# mylist = ['a', 'b', '', 'c', '', 'd']
# mylist = ['a', 'b', '', '', '', 'd']
# print(remove_blanks(mylist))


# Problem 13
# Write a function that takes n as a parameter and returns n factorial.
# n! = n*(n-1)*(n-2)*...*2*1
# 5! = 5*4*3*2*1
# 9! = 9*8*7*6*5*4*3*2*1


def average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)


def factorial(n):
    output = 1
    for x in range(1, n+1):
        output *= x
        # print(x)
    return output


print(factorial(5))  # 120


def factorial_list(n):
    '''returns a list of the first n factorial numbers'''
    # make a blank list to return as our final output
    output = []
    # iterate n times
    for value in range(1, n+1):
        # call factorial for each value
        # append the factorial to our output
        output.append(factorial(value))
    # return the output
    return output


print(factorial_list(5))  # [1, 2, 6, 24, 120]





# Problem 11
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.

def combine_all(mylists):
    new_list = []

    # Solution1
    # for mylist in mylists:
    #     for num in mylist:
    #         new_list.append(num)

    # Solution2
    # for num in nums:
    #   new_list.extend(num)

    # Solution3
    # for num in nums:
    #   new_list += num

    return new_list
# print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]







def list_contains(mylist, myvalue):

    # return myvalue in mylist

    for element in mylist:
        if element == myvalue:
            return True
    return False

print(list_contains([1, 2, 3], 2)) # True
print(list_contains([1, 2, 3], 4)) # False


# Problem 14
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.

def find_unique(nums):
    # Solution1
    new_list = []

    for num in nums:
        # if not (num in new_list):
        if num not in new_list:
            new_list.append(num)
    
    # loop over the numbers in the input list
    for num in nums:
        # check if the output list contains the number that we're looking at
        found = False
        for output_num in new_list:
            if num == output_num:
                found = True
                break
        if not found:
            new_list.append(num)



    return new_list


nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums)  # [12, 24, 35, 88, 120, 155]
print(unique_nums)
