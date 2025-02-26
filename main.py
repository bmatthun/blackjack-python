import sys
import art
import random

print(art.logo)

cards = []

for number in range(14):
    cards.append(4)

def select_card():
    card = -1
    while card != 0:
        random_index = random.randint(0, 13)
        if cards[random_index] != 0:
            cards[random_index] -= 1
            if random_index > 8 and random_index != 13:
                card = 10
            elif random_index == 13:
                card = 11
            else:
                card = random_index + 1
            break
    return card


start_game = input('''Dear Player!
Welcome to the Black Jack game! 
Would you like to play? [y, n]
''')

if start_game == "n":
    sys.exit()

else:
    name = input('''
Good!
Now please enter your name:
''')

    #First game
    player_cards = []
    dealer_cards = []
    for deal in range(4):
        if deal < 2:
            player_cards.append(select_card())
        else:
            dealer_cards.append(select_card())

    print(player_cards, dealer_cards)
    print(cards)


