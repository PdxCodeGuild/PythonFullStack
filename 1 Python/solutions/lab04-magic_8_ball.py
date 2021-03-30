
import random


# begin looping
# ask the user for a question
# show them a random answer
# go to the start of the loop

def shake_magic_8_ball():
    answers = [
        'It is certain',
        'It is decidedly so',
        'Without a doubt',
        'Yes definitely',
        'You may rely on it',
        'As I see it, yes',
        'Most likely',
        'Outlook good',
        'Yes',
        'Signs point to yes',
        'Reply hazy try again',
        'Ask again later',
        'Better not tell you now',
        'Cannot predict now',
        'Concentrate and ask again',
        'Don\'t count on it',
        'My reply is no',
        'My sources say no',
        'Outlook not so good',
        'Very doubtful'
    ]
    return random.choice(answers)


title = 'Welcome to the Magic 8 Ball!'
print('~'*80)
print(' '*(40-len(title)//2) + title)
print('~'*80)

while True:
    question = input('Enter your question or \'done\': ').lower().strip()
    if question in ['done', 'quit', 'exit']:
        print('Thank you for playing!')
        break
    answer = shake_magic_8_ball()
    print('The magic 8 ball says: ' + answer)
