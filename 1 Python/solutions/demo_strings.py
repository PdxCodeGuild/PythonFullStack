



# age = int(input('what is your age?\n> '))


# age = input('what is your age? ')
# age_next_year = int(age) + 1
# print(type(age_next_year))
# print('Next year you\'ll be ' + str(age_next_year))



# print('hello')
# print('hello', 'world', 5, None)
# print('hello', 'world', 5, None, sep='-')

# print('hello', end='_')
# print('world')


# fruits = ['apples', 'bananas', 'pears']
# i = 0
# while i < len(fruits):
#     print(fruits[i], end=' ')
#     i += 1


#            0          1         2       3
# fruits = ['apples', 'bananas', 'pears']
# i = 0
# while i < 100:
#     print(f'{i}%{3}={i%3}', fruits[i%len(fruits)])
#     i += 1


# print('~'*80)
# print(' ' * 36 + 'hello')
# print('~'*80)


# import chalk

# cat_art = '''
#       |\      _,,,---,,_
# ZZZzz /,`.-'`'    -.  ;-;;,_
#      |,4-  ) )-,_. ,\ (  `'-'
#     '---''(_/--'  `-'\_)
# '''

# print(chalk.green(cat_art))



# age = int(input('what is your age? '))
# print(f'Next year you\'ll be {age + 1}')


# color = 'red'
# print(f'The {color} Dragon is the {Superlative} Dragon of all. It has {Adjective1} {Body_parts}, and a {Body_part} shaped like a {Noun}. It loves to eat {Animal}, although it will feast on nearly anything. It is {Adjective2} and {Adjective3}. You must be {Adjective4} around it, or you may end up as it`s meal!')


# import random
# temperature = random.randint(50, 100)
# print(temperature)
# if temperature < 60:
#     print('cold')
# elif temperature < 80:
#     print('warm')
# else:
#     print('hot')




# def min(a, b):
#     # if a < b:
#     #     return a
#     # return b

#     return a if a < b else b
# print(min(5, 2)) # 2


# name = 'bob'
# if name == 'bob':
#     print('your name is bob')

# print(name == 'bob')




# truthy / falsey
# everything is 'truthy' except False, 0, 0.0, None, [], {}


# values = [None, True, False, -1, 0, 1, 5.0, 0.0, [], [1,2,3], {}, {'apples': 1}]
# for value in values:
#     if value:
#         print(value, 'is truthy')
#     else:
#         print(value, 'is falsey')

import random
x = random.randint(-1, 1) # -1, 0, or 1
# if x: # ambgiuous
if x != 0:
    print(x, 'is truthy')



