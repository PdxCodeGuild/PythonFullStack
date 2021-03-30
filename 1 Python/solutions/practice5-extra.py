


# Problem 1: Pretty Numbers
# Convert an integer into a pretty string with commas 12345678 to 12,345,678


# indices: 0123456789
# number:  1653872151

#         0 123 456 789
# output: 1,653,872,151



def pretty_number(num):
    num = str(num)
    num = list(num)
    num.reverse()
    output = []
    for i in range(len(num)):
        output.append(num[i])
        # if you're at an increment of 3
        # and NOT on the last iteration
        # add a comma
        if (i+1)%3 == 0 and i+1 < len(num):
            output.append(',')
    output.reverse()
    output = ''.join(output)
    return output

    # num = str(num)
    # output = ''
    # for i in range(len(num)-1, -1, -1):
    #     output = num[i] + output
    #     if (len(num)-i)%3 == 0 and i != 0:
    #         output = ',' + output
    # return output

    # num = str(num)
    # output = ''
    # for i in range(len(num)//3, -1, -1):
    #     output = ',' + num[i*3: i*3+3] + output
    # return output
    


#                    indices       9 876 543 210
# print(pretty_number(1653872151)) # 1,653,872,151
# print(pretty_number(2358109322348520)) # 2,358,109,322,348,520
# print(pretty_number(999999)) # 999,999
# print(pretty_number(0)) # 0
# print(pretty_number(999)) # 999
# print(pretty_number(10000)) # 10,000



# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
# 

def fibonacci(n):
    output = []
    for i in range(n):
        if i == 0 or i == 1:
            output.append(1)
        else:
            output.append(output[i-1] + output[i-2])
            # output.append(output[-1] + output[-2])
    
    # if n == 1:
    #     return [1]
    # output = [1, 1]
    # for i in range(n-2):
    #     output.append(output[-1] + output[-2])


    return output


# print(fibonacci(1)) # [1]
# print(fibonacci(2)) # [1, 1]

# print(fibonacci(8))  # [1, 1, 2, 3, 5, 8, 13, 21]
# print(fibonacci(10)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]



# Problem 3: Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse. Write a function check_palindrome(word) which takes a string, and returns True if the string's a palindrome, or False if it's not.

def check_palindrome(word):
    # convert the word to a list of characters
    flist = list(word) # ['r', 'a', 'c', 'e', 'c', 'a', 'r']
    # reverse the list of characters
    flist.reverse()
    # join the characters back into a single string
    reversed_word = ''.join(flist)
    # compare the original string with the reversed string
    return word == reversed_word
    # if word == reversed_word:
    #     return True
    # else:
    #     return False

    # return word == word[::-1]


# print(check_palindrome('racecar')) # True
# print(check_palindrome('palindrome')) # False


# def check_palindrome2(word):
#     for i in range(len(word)//2):
#         j = len(word) - 1 - i
#         # i will go 0, 1, 2
#         # j will go 6, 5, 4
#         print(word[i], word[j])
#         if word[i] != word[j]:
#             return False
#     return True
        
# #                        0123456
# print(check_palindrome2('racecar')) # True
# print(check_palindrome2('palindrome')) # False