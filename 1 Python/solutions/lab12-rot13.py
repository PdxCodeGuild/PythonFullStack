

import string


def rot13_approach1(text):
    alphabet =         'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = 'nopqrstuvwxyzabcdefghijklm'

    # alphabet = string.ascii_lowercase
    # rotated_alphabet = alphabet[13:] + alphabet[:13]
    # rotated_alphabet = alphabet[len(alphabet)//2:] + alphabet[:len(alphabet)//2]
    
    output = ''
    for char in text:
        index = alphabet.find(char)
        output += rotated_alphabet[index]
    return output

# print(rot13_approach1('hello')) # uryyb


def rotn_approach2(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n
        index %= len(alphabet)

        # if index > len(alphabet):
        #     index -= len(alphabet)
        
        # while index > len(alphabet):
        #     index -= len(alphabet)
        # while index < 0:
        #     index += len(alphabet)

        output += alphabet[index]
    return output
        
# print(rotn_approach2('hello', 10)) # rovvy
# print(rotn_approach2('rovvy', -10)) # hello     


def rotn_approach3(text, n):

    output = ''
    for char in text:
        ascii_code = ord(char)
        print(char, ascii_code)
        ascii_code -= ord('a')
        ascii_code += n
        ascii_code %= 26
        ascii_code += ord('a')
        output += chr(ascii_code)

    return output

# print(rotn_approach3('hello', 13))


def rotn_approach4(text, n):

    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + ' '
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n
        index %= len(alphabet)
        output += alphabet[index]

    return output

# print(rotn_approach4('Hello World! 123 abc!@#!@#', 13))
# print(rotn_approach4('UryyBm9BEyq.m%&\'mnop.b:.b:', -13))



def rotn_approach5(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += n
            index %= len(alphabet)
            output += alphabet[index]
    return output


# print(rotn_approach5('Hello World! 123 abc!@#!@#', 13))
# print(rotn_approach5('Hryyb Wbeyq! 123 nop!@#!@#', -13))


def rotn_approach6(text, n):
    alphabet_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_uppercase = alphabet_lowercase.upper()
    output = ''
    for char in text:
        index_lowercase = alphabet_lowercase.find(char)
        index_uppercase = alphabet_uppercase.find(char)
        if index_lowercase != -1:
            index_lowercase += n
            index_lowercase %= len(alphabet_lowercase)
            output += alphabet_lowercase[index_lowercase]
        elif index_uppercase != -1:
            index_uppercase += n
            index_uppercase %= len(alphabet_uppercase)
            output += alphabet_uppercase[index_uppercase]
        else:
            output += char
    return output


# print(rotn_approach6('Hello World! 123 abc!@#!@#', 13))
# print(rotn_approach6('Uryyb Jbeyq! 123 nop!@#!@#', -13))


# import random

# nums = []
# for i in range(6):
#     nums.append(random.randint(1, 99))
# print(nums)


# nums = [random.randint(1, 99) for i in range(6)]
# print(nums) # [9, 89, 82, 1, 23, 76]

# nums = [str(i+10) + '!' for i in range(6)]
# print(nums) # ['10!', '11!', '12!', '13!', '14!', '15!']

# nums = [i for i in range(6) if i%2 == 0]
# print(nums) # [0, 2, 4]



def rotn_approach7(text, n):
    print([ord(char) for char in text])
    print([ord(char)-97 for char in text])
    print([ord(char)-97+n for char in text])
    print([(ord(char)-97+n)%26 for char in text])
    print([(ord(char)-97+n)%26+97 for char in text])
    print([chr((ord(char)-97+n)%26+97) for char in text])
    return ''.join([chr((ord(char)-97+n)%26+97) for char in text])

print(rotn_approach7('hello', 13))


