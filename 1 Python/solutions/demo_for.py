
import random

nums = []
for i in range(100):
    nums.append(random.randint(1000, 3000))
nums.append(2000)
random.shuffle(nums)

for num in nums:
    if num == 2000:
        print('found 2000')
    else:
        print('nope')



