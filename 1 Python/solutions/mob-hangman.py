

import random
import requests
import string


hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \. |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
=========''']

# response = requests.get('https://random-word-api.herokuapp.com/word?swear=0')
# print(response.json()[0])


def get_random_word():

    response = requests.get('https://random-word-api.herokuapp.com/word?swear=0')
    return response.json()[0]

    # # download word list
    # response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_bumble_bee/main/1%20Python/labs/data/english.txt')
    # # check if there was an error
    # if response.status_code != 200:
    #     print('error retrieving word list')
    #     exit()
    # # split the text into words
    # word_list = response.text.split('\n')
    # # pick a random word
    # random_word = random.choice(word_list)
    # return random_word


#  01234
# 'hello'
#   0    1    2    3    4
# ['_', '_', '_', '_', '_']
# user guesses l
#   0    1    2    3    4
# ['_', '_', 'l', '_', '_']


# chosen word
chosen_word = get_random_word()
# counter for the number of guessed so far
guess_counter = 0
wrong_counter = 0
# the letters we've already guessed
guessed_letters = []
# letters to replace
letters_and_underscores = ['_']*len(chosen_word)

# letters_and_underscores = []
# for i in range(len(chosen_word)):
#     letters_and_underscores.append('_')

# begin our game loop
while True:
    # show the hangman ascii art
    print(hangman_pics[wrong_counter])
    # print out underscores
    print(' '.join(letters_and_underscores))
    # print out what the user has already guessed
    print('Guessed letters: ' + ' '.join(guessed_letters))
    # prompt the user for a letter
    letter = input('Guess a letter: ').lower().strip()
    guess_counter += 1
    if letter == chosen_word:
        print()
        print('You win! ' + '~'*20)
        print('The word was \'' + chosen_word + '\'')
        print(f'It took {guess_counter} guesses with {wrong_counter} wrong guesses')
        print('You\'re free!')
        print(hangman_pics[0])
        exit()
    # ensure the user actually entered a letter
    if letter not in string.ascii_lowercase or len(letter) != 1:
        print('invalid input')
        continue
    # check is letter is in our previously guessed letters list
    if letter in guessed_letters:
        print('you already guessed that!')
        continue
    # add the letter to our list of guessed letters
    guessed_letters.append(letter)
    # guessed_letters.sort()
    # check if letter is in chosen word
    if letter in chosen_word:
        # do not increase the guess counter
        # find the indices of the letter in the chosen word
        # change the corresponding underscore into the letter
        found_counter = 0
        for i in range(len(chosen_word)):
            if letter == chosen_word[i]:
                letters_and_underscores[i] = chosen_word[i]
                found_counter += 1
        print(f'There were {found_counter} instances of the letter \'{letter}\' in the word')

        # check if we won
        # if letters_and_underscores == list(chosen_word):
        if ''.join(letters_and_underscores) == chosen_word:
            print()
            print('You win! ' + '~'*20)
            print('The word was \'' + chosen_word + '\'')
            print(f'It took {guess_counter} guesses with {wrong_counter} wrong guesses')
            print('You\'re free!')
            print(hangman_pics[0])
            exit()
    else:
        print('There\'s no \'' + letter + '\' in the word')
        # increment our wrong guesses counter
        wrong_counter += 1
        # check if we lost
        if wrong_counter == 10:
            print('Game over! Keep hanging in there.')
            print('The word was \'' + chosen_word + '\'')
            print(f'It took {guess_counter} guesses with {wrong_counter} wrong guesses')
            print(hangman_pics[10])
            exit()
