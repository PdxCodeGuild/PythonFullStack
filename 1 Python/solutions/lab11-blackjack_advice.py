

card_values = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}

def get_card():
    while True:
        print('Enter a card: ' + ', '.join(card_values.keys()))
        card = input('> ').upper().strip()
        if card in card_values:
            return card
        else:
            print(card + ' is not a valid card')

card1 = get_card()
card2 = get_card()
card3 = get_card()

total = card_values[card1] + card_values[card2] + card_values[card3]
# if 'A' in [card1, card2, card3]:
if (card1 == 'A' or card2 == 'A' or card3 == 'A') and total + 10 <= 21:
    print('Counting an ace as 11 instead of 1')
    total += 10

print(f'The total for your cards is {total}')
if total < 17:
    print('Hit!')
elif total < 21:
    print('Stay!')
elif total == 21:
    print('Blackjack!')
else:
    print('Bust!')


