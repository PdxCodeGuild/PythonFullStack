

import random

import time





# message = 'hello world!'
# for char in message:
#     print(char, end='', flush=True)
#     time.sleep(0.1)



# for i in range(0, 100):
#     print(int(2.7182818284**i)%11)

# random.seed(int(time.time()*1000))

# for i in range(10):
#     print(random.randint(0,10))





def random_list(n):
    '''Generates a list of random numbers'''
    random_list = []
    for _ in range(n):
        random_list.append(random.randint(0,99))
    return random_list




# Fisher-Yates Shuffle

# iterate through the indices of the list
# for each iteration, generate a random index
# swap the elements at the two indices

# for i from 0 to n−1 do
#      j ← random integer such that i ≤ j < n
#      exchange a[i] and a[j]

#  i        j
# [1, 2, 3, 4, 5, 6]
# [4, 2, 3, 1, 5, 6]

#  j  i
# [4, 2, 3, 1, 5, 6]
# [2, 4, 3, 1, 5, 6]

#        i        j
# [2, 4, 3, 1, 5, 6]
# [2, 4, 6, 1, 5, 3]

def shuffle(nums):
    '''Randomly re-arranges a list'''
    for i in range(0,len(nums)):
        j = random.randint(i,len(nums)-1)
        # print(f"i:{i} j:{j}")  
        t_num = nums[i] 
        nums[i] = nums[j]
        nums[j] = t_num

        # nums[i], nums[j] = nums[j], nums[i]
    



def is_sorted(nums):
    '''Checks if a list is sorted'''
    for i in range(len(nums)):
        if i + 1 < len(nums) and nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):   
    '''bogosort(nums) continues to generate random arrangements until the list is sorted'''
    while not is_sorted(nums):
        shuffle(nums)


nums = random_list(8)
# nums.sort()
print(nums)
# shuffle(nums)
# print(is_sorted(nums))
bogosort(nums)
print(nums)


