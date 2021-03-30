import math

# class Point:
#     def __init__(self, x, y): # this is the initializer
#         self.x = x # these are member variables
#         self.y = y

#     def distance(self, p): # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)

# p1 = Point(5, 2) # call the initializer, instantiate the class
# p2 = Point(8, 4)
# print(p1.x) # 5
# print(p1.y) # 2
# print(type(p1)) # Point
# print(p1.distance(p2))


# class str:
#     def __init__(self, value):
#         ...
#     def split(self, delimiter):
#         ...

# x = str(5)
# fruits = 'apples, bananas, pears'
# fruits.split(', ')


# class list:
#     def __init__(self, value):
#         ...
#     def append(element):
#         ...

# nums = list('abc') # ['a', 'b', 'c']
# nums.append('d')
# print(nums) # ['a', 'b', 'c', 'd']

# import requests
# response = requests.get('https://www.google.com/')
# print(type(response))
# print(response.status_code)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def distance(self, p): # method, or 'member function'
#         dx = self.x - p.x
#         dy = self.y - p.y
#         return math.sqrt(dx*dx + dy*dy)

#     def scale(self, v):
#         self.x = self.x*v
#         self.y = self.y*v

#     def __str__(self):
#         return f'({self.x},{self.y})'


# p = Point(5, 2)
# print(p)
# p.scale(5)
# print(p)


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next is not None})'


class Stack:
    def __init__(self):
        self.root = None
    
    def push(self, element):  # insert an element at the start (new root)

        if self.root is None: # check if the root node is None (the stack is empty)
            self.root = Node(element, None) # if it is, create a new root node
        else: # otherwise
            # create a new node pointing to the root
            node = Node(element, self.root)
            # make the root the new node
            self.root = node
        
        # one-liner
        # self.root = Node(element, self.root)


    def pop(self):  # remove an element from the start (the root becomes the next node)
        ...

    def peek(self):  # returns the element on the root node or None if there is no root
        ...

    def length(self):  # return the number of elements
        ...

    def __str__(self):
        output = ''
        n = self.root
        while n is not None:
            output += f'({n.item},{n.next is not None}) '
            n = n.next
        return output


s = Stack()
s.push('apples')
s.push('bananas')
s.push('pears')
print(s)
