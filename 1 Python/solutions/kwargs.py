


def total(nums):
    print(nums)
    output = 0
    for num in nums:
        output += num
    return output
print(total([1, 2, 3])) # 6

def total_args(*nums):
    print(nums)
    output = 0
    for num in nums:
        output += num
    return output
print(total_args(1, 2, 3)) # 6


def say_hello(person):
    print(person)
    print(person['name'] + ' says hello!')

say_hello({'name': 'Bob', 'age': 45})


def say_hello_kwargs(**person):
    print(person)
    print(person['name'] + ' says hello!')
say_hello_kwargs(name='Bob', age=45)





