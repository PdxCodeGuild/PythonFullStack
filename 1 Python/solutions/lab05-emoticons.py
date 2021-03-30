
import random

def generate_eastern_emoji():
    sides_list = [
        ['(', ')'],
        ['[', ']'],
        ['{', '}']
    ]
    eyes_list = ['O', 'o', '^', '-', '°']
    mouth_list = ['_', 'o', 'w']
    
    sides = random.choice(sides_list)
    eyes = random.choice(eyes_list)

    mouth = random.choice(mouth_list)
    while (eyes == 'o' or eyes == 'O') and mouth == 'o':
        mouth = random.choice(mouth_list)
    
    if random.randint(1,10) == 1:
        return sides[0] + eyes + mouth + eyes + ';' + sides[1]
    return sides[0] + eyes + mouth + eyes + sides[1]


for i in range(100):
    print(generate_eastern_emoji())





