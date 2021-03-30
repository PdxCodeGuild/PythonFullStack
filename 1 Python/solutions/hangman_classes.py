
import requests


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

class HangmanGame:
    def __init__(self):
        self.secret_word = ''
        self.underscores = []
        self.guessed_letters = []
        self.hangman_pics = hangman_pics
        self.wrong_guesses = 0
        self.reset()
    
    def reset(self):
        response = requests.get('https://random-word-api.herokuapp.com/word?swear=0')
        self.secret_word = response.json()[0]
        self.underscores = ['_']*len(self.secret_word)
        self.guessed_letters = []
        self.wrong_guesses = 0
    
    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print('You already guessed \'' + letter + '\'')
            return
        self.guessed_letters.append(letter)
        if letter not in self.secret_word:
            print('Letter not found')
            self.wrong_guesses += 1
            return
        for i in range(len(self.secret_word)):
            if self.secret_word[i] == letter:
                self.underscores[i] = letter
    
    def check_win(self):
        return self.secret_word == ''.join(self.underscores)

    def display(self):
        print(self.hangman_pics[self.wrong_guesses])
        print(' '.join(self.underscores))
        print('guessed letters: ' + ' '.join(self.guessed_letters))



game = HangmanGame()
while True:
    game.display()
    letter = input('enter a letter: ')
    game.guess_letter(letter)
    if game.check_win():
        print('You won!')
        break
    






