


import random
import math

def mean(nums):
    # return sum(nums)/len(nums)

    total = 0
    for num in nums:
        total += num
    return total / len(nums)


def variance(nums):
    m = mean(nums)
    total = 0
    for num in nums:
        total += (num - m)**2
    return total / len(nums)


def standard_deviation(nums):
    return math.sqrt(variance(nums))
    # return variance(nums)**0.5


nums = [random.randint(0,99) for i in range(100)]

print('mean:', mean(nums))
print('variance:', variance(nums))
print('standard deviation:', standard_deviation(nums))




