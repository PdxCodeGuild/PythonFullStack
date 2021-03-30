

import random
import time

# def get_number():
#     while True:
#         number = input('enter a number between 1 and 10: ')
#         if number.isdigit() or 1 <= int(number) <= 10:
#             return number
# number = get_number()
# print(number)



# Version 1 ==================================================

# number = random.randint(1, 10)
# guesses = 0
# while guesses < 10:
#     guess = int(input('Guess the number: '))
#     guesses += 1
#     if guess == number:
#         print(f'Correct! You took {guesses} guesses.')
#         break
#     else:
#         print(f'Incorrect! You have {10-guesses} remaining.')
# if guesses == 10:
#     print('You lose!')


# number = random.randint(1, 10)
# guessed = False
# for i in range(1, 11):
#     guess = int(input('Guess the number: '))
#     if guess == number:
#         print(f'Correct! You took {i} guesses')
#         guessed = True
#         break
# if not guessed:
#     print('You lose!')


# number = random.randint(1, 10)
# for i in range(1, 11):
#     guess = int(input('Guess the number: '))
#     if guess == number:
#         print(f'Correct! You took {i} guesses')
#         break
# else: # the else will run if you don't break
#     print('You lose!')


# Version 2+3 ===================================================



# number = random.randint(1, 10)
# guessed = []
# guesses = 0
# while True:
#     guess = int(input('Guess the number: '))
#     guesses += 1
#     if guess in guessed:
#         print('You already guessed that!')
#         continue
#     guessed.append(guess)

#     if guess == number:
#         print(f'You won! It took {guesses} guesses')
#         break
#     elif guess < number:
#         print('Too low!')
#     elif guess > number:
#         print('Too high!')



# Version 4 ==================================================

# number = random.randint(1, 10)
# print(number)
# guessed_list = [] # list of guessed number
# guesses = 0 # counter for the number of guesses
# while True:
#     # get the guess from the user
#     guess = int(input('Guess the number: '))
#     # increment our guess counter
#     guesses += 1

#     # if the user already guessed that number, tell them and restart the loop
#     if guess in guessed_list:
#         print('You already guessed that!')
#     guessed_list.append(guess)
    
#     if guess == number: # if the guess the right number, break
#         print(f'You won! You took {guesses} guesses')
#         break
#     elif len(guessed_list) >= 2: # if we have at least two guesses
#         distance_current_guess = abs(guessed_list[-1] - number)
#         distance_last_guess = abs(guessed_list[-2] - number)
#         # if the current guess is closer than the last guess
#         if distance_current_guess < distance_last_guess:
#             print('Warmer')
#         elif distance_current_guess > distance_last_guess:
#             print('Colder')
#         else:
#             print('Same distance')
    


# Version 5 ==============================================


# print('Think of a number between 1 and 10...')
# guess_counter = 0
# time.sleep(5)
# for i in range(1, 11):
#     guess_counter += 1
#     correct = input(f'Is it {i}? y/n ').lower()
#     if correct == 'y':
#         print(f'I won in {guess_counter} guesses')
#         break



lower_bound = 1
upper_bound = 1000
print(f'Think of a number between {lower_bound} and {upper_bound}...')
time.sleep(5)
guess_counter = 0
while True:
    guess = (lower_bound + upper_bound) // 2
    guess_counter += 1
    correct = input(f'Is is {guess}? ').lower().strip()
    if correct in ['y', 'yes', 'yup', 'yeah']:
        print(f'I won in {guess_counter} guesses')
        break
    higher_lower = input(f'Is the number higher or lower than {guess}? ').lower().strip()
    if higher_lower == 'higher':
        lower_bound = guess + 1
    else:
        upper_bound = guess - 1





