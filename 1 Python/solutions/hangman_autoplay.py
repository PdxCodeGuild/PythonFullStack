

import requests
import random



def pad(text, length):
    if len(text) < length:
        return text + ' '*(length-len(text))
    return text

response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_bumble_bee/main/1%20Python/labs/data/english.txt')
words = response.text.split('\n')
letters = response.text.replace('\n','')
frequencies = {} # {'a': 45, 'b': 23, 'c': 67}
for letter in letters:
    if letter in frequencies:
        frequencies[letter] += 1
    else:
        frequencies[letter] = 1


# def add(a, b):
#     return a + b
# print(add(5, 2)) # 7

# add = lambda a, b: a + b
# print(add(5, 2)) # 7


frequencies = list(frequencies.items())
frequencies.sort(key=lambda x: x[1], reverse=True)
# letters = []
# for f in frequencies:
#     letters.append(f[0])
letters = [f[0] for f in frequencies]

print(' '.join(letters))

total_games = 1000
wins = 0

# uncomment to lost every game
# letters.reverse()

print(pad('word', 15) + '\tguesses\twrong')
for i in range(total_games):
    chosen_word = random.choice(words)
    underscores = ['_']*len(chosen_word)
    guess_counter = 0
    wrong_counter = 0
    # uncomment to see if we're doing better than guessing random letters
    # random.shuffle(letters) 
    for letter in letters:
        guess_counter += 1
        if letter in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == letter:
                    underscores[i] = letter
            if ''.join(underscores) == chosen_word:
                if wrong_counter < 10:
                    wins += 1
                break
        else:
            wrong_counter += 1
    print(pad(chosen_word, 15) + '\t' + str(guess_counter) + '\t' + str(wrong_counter))


print(f'{wins} wins out of {total_games} games')


