

import string


# Problem 1
# Get a string from the user, print out another string, doubling every letter.


def double_letters(word):
    output = ''
    for char in word:
        output += char + char
    return output


def multiply_letters(word, n):
    # accumulator pattern
    output = ''
    for char in word:
        # output += char + char
        output += char * n
    return output

    # return ''.join([char*2 for char in word])

# print(multiply_letters('hello', 40)) # hheelllloo


# Problem 2 ========================================
# Return the number of letter occurances in a string.

def count_letter(letter, word):

    total = 0
    for char in word:
        if char == letter:
            total += 1
    return total


    # return word.count(letter)

    # initial_length = len(word)
    # word = word.replace(letter, '')
    # final_length = len(word)
    # return initial_length - final_length

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2


# Problem 3
# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):

    # option 1 - sort and take the latest letter

    word_list = list(word)
    word_list.sort()
    return word_list[-1]

    # option 2 - convert to ascii code, find the largest ascii value
    # convert to lower case first

    # word = word.lower()
    # highest = 0
    # for char in word:
    #     if ord(char) > highest:
    #         highest = ord(char)
    # return chr(highest)

    # option 3 - combine options 1 and 2
    # codes = []
    # for char in word:
    #     codes.append(ord(char))
    # codes.sort()
    # return chr(codes[-1])

    # option 4 - use the alphabet and .find
    # alphabet = string.ascii_lowercase
    # highest = 'a'
    # for char in word:
    #     if alphabet.find(char) > alphabet.find(highest):
    #         highest = char
    # return highest
    
# print(latest_letter('Pneumonoultramicroscopicsilicovolcanoconiosis')) # v
# print(latest_letter('aZ')) # a


# Problem 4 ====================================================================
# Write a function that returns the number of occurances of 'hi' in a given string.

def count_hi(text):
    # variable = text.count("hi")
    # return variable


    # count = 0
    # for i in range(len(text)):
    #     if i < len(text) - 1 and text[i] + text[i + 1] == 'hi':
    #         count += 1

    # return count

    # count = 0
    # for i in range(len(text)-1):
    #     print(i,text[i],text[i+1])
    #     # if i < len(text) - 1 and text[i] + text[i + 1] == 'hi':
    #     # if text[i] + text[i + 1] == 'hi':
    #     if text[i] == 'h' and text[i+1] == 'i':
    #         count += 1
    # return count

    return (len(text) - len(text.replace('hi', '')))//2
    # return len(text) - len(text.replace('hi', ' '))


# print(count_hi('hihi')) # 2
# print(count_hi('ahibchi')) # 2
# print(count_hi('hi hello hi hello test 123 abc hi')) # 3




# this_is_snake_case - python variables and functions
# this-is-kebab-case - css classes
# thisIsCamelCase - java variables, used in JavaScript
# ThisIsTitleCaseOrPascalCase - python classes
# THIS_IS_SCREAM_CASE - global constants


# Problem 5
# Write a function that converts text to snake case (all lowercase, underscores for spaces, no special characters).

import string
def snake_case(text):

    # text = text.lower()
    # for char in string.punctuation:
    #     text = text.replace(char, '')
    # text = text.replace(' ', '_')
    # return text

    changing = text.replace(' ', '_').replace('-', '_').lower().strip(string.punctuation)
    return changing

# print(snake_case('Hello World!')) # hello_world
# print(snake_case('This is another example.')) # this_is_another_example


# Problem 6
# Write a function that converts text to camel case (no spaces, no special characters, leading capitals except the first).

# #            0          1        2
# fruits = ['apples', 'bananas', 'pears']

# # iterating over the elements of a list
# for fruit in fruits:
#     print(fruit)
#     fruit += '!' # does nothing

# print(fruits)

# # iterate over the indices of a list
# for i in range(len(fruits)):
#     print(i, fruits[i])
#     fruits[i] += '!' # modifies the element at that index, fruits[i] = fruits[i] + '!'

# print(fruits)



def camel_case(text):
    text = text.strip(string.punctuation)
    changing = text.split(' ')
    for i in range(len(changing)):
        if i != 0:
            changing[i] = changing[i].title()
        else:
            changing[i] = changing[i].lower()
    return ''.join(changing)
print(camel_case('Hello World!')) # helloWorld
print(camel_case('This is another example.')) # thisIsAnotherExample