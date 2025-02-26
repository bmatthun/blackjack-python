import sys
import art
import random

print(art.logo)

cards = []
score = {
    "player": 0,
    "dealer": 0
}

for number in range(14):
    cards.append(4)

def select_card():
    actual_card = -1
    while actual_card != 0:
        random_index = random.randint(0, 13)
        if cards[random_index] != 0:
            cards[random_index] -= 1
            if random_index > 8 and random_index != 13:
                actual_card = 10
            elif random_index == 13:
                actual_card = 11
            else:
                actual_card = random_index + 1
            break
    return actual_card

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

    print('''
Let\'s play!
''')

    game_is_on = True

    while game_is_on:
        #First round
        first_round = True
        player_cards = []
        dealer_cards = []
        for deal in range(4):
            if deal < 2:
                player_cards.append(select_card())
            else:
                dealer_cards.append(select_card())

        print(f"Your cards: {player_cards}, dealer's cards: [{dealer_cards[0]}, X]")

        if first_round and sum(player_cards) > 20:
            print("Wow! Nice hands! ;) You won!!")
            score["player"] += 1
            another_round = input("Another round? [y, n]")
            if another_round == "y":
                continue
            elif another_round == "n":
                sys.exit()
            else:
                print("Say what?")

        first_round = False

        game_continue = input("Hit or Stop? [h, s]\n")
        another_round = False

        while game_continue == "h":
            another_round = False
            player_cards.append(select_card())
            if sum(player_cards) > 21:
                print(f"Your cards: {player_cards}, dealer's cards: [{dealer_cards[0]}, X]")
                if 11 in player_cards:
                    print(f"The sum value of your cards in hand are greater than 21, the value of Ace will be reduced from 11 to 1! :)")
                    for card in player_cards:
                        if card == 11:
                            card -= 10
                    print(f"Your cards after the cutting the value of the Ace: {player_cards}, dealer's cards: [{dealer_cards[0]}, X]")
                else:
                    another_round = input("You've lost! :/ Another round? [y, n]")
                    score["dealer"] += 1
                    if another_round == "y":
                        another_round = True
                        break
                    elif another_round == "n":
                        sys.exit()
                    else:
                        print("Say what?")

            elif sum(player_cards) < 21:
                print(f"Your cards: {player_cards}, dealer's cards: [{dealer_cards[0]}, X]")
                game_continue = input("Hit or Stop? [h, s]\n")
                continue

            else:
                print(f"21!! BlackJack!! Your cards: {player_cards}, dealer's cards: [{dealer_cards[0]}, X]")
                another_round = input("Another round? [y, n]")
                if another_round == "y":
                    another_round = True
                    break
                elif another_round == "n":
                    sys.exit()
                else:
                    print("Say what?")

        if another_round:
            continue

        while sum(dealer_cards) < 17:
            dealer_cards.append(select_card())

        print(f"Your cards: {player_cards}, dealer's cards: {dealer_cards}")
        if sum(dealer_cards) > 21:
            print("You won!! :)")
            score["player"] += 1
            another_round = input("Another round? [y, n]")
            if another_round == "y":
                another_round = True
                continue
            elif another_round == "n":
                sys.exit()
            else:
                print("Say what?")

        elif sum(dealer_cards) < sum(player_cards):
            print("You won!! :)")
            score["player"] += 1
            another_round = input("Another round? [y, n]")
            if another_round == "y":
                another_round = True
                continue
            elif another_round == "n":
                sys.exit()
            else:
                print("Say what?")

        elif sum(dealer_cards) > sum(player_cards):
            print("You Lost!! :((")
            score["dealer"] += 1
            another_round = input("Another round? [y, n]")
            if another_round == "y":
                another_round = True
                continue
            elif another_round == "n":
                sys.exit()
            else:
                print("Say what?")

        else:
            print("DRAW! :O")
            another_round = input("Another round? [y, n]")
            if another_round == "y":
                another_round = True
                break
            elif another_round == "n":
                sys.exit()
            else:
                print("Say what?")

