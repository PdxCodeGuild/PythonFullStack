

# lists are mutable ===================

fruits = ['apples', 'bananas', 'pears']
fruits[0] = 'cherries'

fruits.sort()

fruits.append('avocado')

print(fruits)

# strings are immutable ================

name = 'joe'
# name[0] = 'b' # crash

name = name.replace('j', 'b')
name = name.upper()

print(name)




