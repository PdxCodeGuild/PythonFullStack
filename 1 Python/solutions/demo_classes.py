
import math



# these look like functions, but they're actually initializers for their respective types
# print(int('5')) # 5
# print(int(5.2)) # 5
# print(float('5.2')) # 5.2
# print(str(5)) # '5'

# writing the literal
# x = 0
# y = []
# invoking the initializer
# x = int()
# y = list()


# functions
# print('hello')
# print(ord('a'))

# methods are a special kind of function
# all methods are functions, not all functions are methods
# methods are functions that belong to classes/types
# fruits = ['apples', 'bananas', 'pears']
# fruits.append('kiwi')

# not all "something.function()"'s are methods
# import random
# random.randint(5, 10)



# list literal
# fruits = ['apples', 'bananas', 'pears']
# print(type(fruits))


class Point:
    def __init__(self, x, y): # this is the initializer
        self.x = x # these are member variables
        self.y = y
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
p1 = Point(5, 2) # call the initializer, instantiate the class
print(p1.x) # 5
print(p1.y) # 2
print(type(p1)) # Point
p2 = Point(8, 4)
print(p1.distance(p2))



# ====================================================================




class RotCipher:
    def __init__(self, n):
        self.n = n # add a property to the class instance
    
    def encrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        output = ''
        for char in text:
            index = alphabet.find(char)
            if index == -1:
                output += char
            else:
                index += self.n
                index %= len(alphabet)
                output += alphabet[index]
        return output
    
    def decrypt(self, text):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        output = ''
        for char in text:
            index = alphabet.find(char)
            if index == -1:
                output += char
            else:
                index -= self.n
                index %= len(alphabet)
                output += alphabet[index]
        return output


rot_cipher = RotCipher(13)
print(rot_cipher.n)
text = 'hello'
print(text)
text = rot_cipher.encrypt(text)
# text = RotCipher.encrypt(rot_cipher, text)
print(text)
text = rot_cipher.decrypt(text)
print(text)



