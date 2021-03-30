

import random


def get_nums(n):
    nums = []
    # loop n times
    for i in range(n):
        # generate random numbers until they're unique
        num = random.randint(0, 99)
        while num in nums:
            num = random.randint(0, 99)
        # insert num into the list
        nums.append(num)
    # nums = [random.randint(0, 99) for i in range(n)]
    # nums = list(set(nums))
    nums.sort()
    return nums


#              0          1          2       3
# fruits = ['apples', 'bananas', 'pears', 'kiwi']
# fruits.index('kiwi') # 3
# O(n)

def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return None

# index 0  1  2  3  4  5  6  7
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2
# O(log(n))


def binary_search(nums, target):
    print('searching for ' + str(target))
    low = 0
    high = len(nums) - 1
    while low <= high:
        middle = (low + high) // 2
        print('indices: ' + '   '*low + ' L' + '   ' *(middle-low-1) + '  M' + '   '*(high-middle-1) + '  H')
        print('values:  ' + ' '.join([' ' + str(num) if num < 10 else str(num) for num in nums]))
        if nums[middle] < target:
            low = middle + 1
        elif nums[middle] > target:
            high = middle - 1
        else:
            return middle
    return None


nums = get_nums(30)
print('indices: ' + '  '.join([' ' + str(i) if i < 10 else str(i) for i in range(len(nums))]))
print('values:  ' + ', '.join([' ' + str(num) if num < 10 else str(num) for num in nums]))
for i in range(10):
    index = random.randint(0, len(nums)-1)  # get a random index
    num = nums[index]  # get the number at that index
    found_index = binary_search(nums, num)  # do a linear search
    if index == found_index:  # if we were correct
        print('Got the correct index for ' + str(num))
    else:
        print('Error, expected ' + str(index) + ' got ' + str(found_index))
    print()


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return f'({self.item}, {self.next})'


# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, element):  # insert an element at the start (new root)
#         self.items.append(element)

#     def pop(self):  # remove an element from the start (the root becomes the next node)
#         if len(self.items) == 0:
#             return None
#         return self.items.pop()

#     def peek(self):  # returns the element on the root node or None if there is no root
#         if len(self.items) == 0:
#             return None
#         return self.items[-1]

#     def length(self):  # return the number of elements
#         return len(self.items)

#     def __str__(self):
#         return str(self.items)


class Stack:
    def __init__(self):
        self.root = None

    def push(self, element):  # insert an element at the start (new root)
        # if self.root is None: # check if the stack is empty
        #     self.root = Node(element) # create a new root with no 'next' node
        # else:
        #     new_root = Node(element, self.root) # create a new root node pointing at the old root
        #     self.root = new_root # assign the new root to our stack's root

        self.root = Node(element, self.root)

    def pop(self):  # remove an element from the start (the root becomes the next node)
        if self.root is None:
            return None
        item = self.root.item
        self.root = self.root.next
        return item

    def peek(self):  # returns the element on the root node or None if there is no root
        if self.root is None:
            return None
        return self.root.item

    def length(self):  # return the number of elements
        count = 0
        n = self.root
        while n is not None:
            count += 1
            n = n.next
        return count

    def __str__(self):
        output = ''
        n = self.root
        while n is not None:
            output += f'{n.item}->'
            n = n.next
        return output


s = Stack()
s.push('apples')
print(s)
s.push('bananas')
print(s)
s.push('pears')
print(s)
print(s.length())  # 3
print(s.pop())  # 'pears'
print(s)
print(s.pop())  # 'bananas'
print(s)
print(s.peek())


class LinkedList:
    def __init__(self):
        self.root = None

    def append(self, element):  # add the element to the end
        if self.root is None: # if the list is empty
            self.root = Node(element) # create a new root node
        else:
            # looping until we find the last node
            n = self.root # set our temporary node to the root
            while n.next is not None: # while the next node of our temporary is None
                n = n.next # advance our temporary node
            n.next = Node(element) # set the next node of the last node to a new node containing our element


    def insert(self, element, index):  # insert the element at the given index
        ...

    def remove(self, element):  # remove the first occurrence of the element
        ...

    def get(self, index):  # get the element at the given index (starting with 0)
        ...

    def find(self, element):  # find the first occurrence of the element and return it
        ...

    def length(self):  # return the length of the list
        ...
    
    def __str__(self):  # return the length of the list
        output = ''
        n = self.root
        while n is not None:
            output += f'{n.item}->'
            n = n.next
        return output


nums = LinkedList()
nums.append(5)
nums.append(6)
nums.append(7)
print(nums)
