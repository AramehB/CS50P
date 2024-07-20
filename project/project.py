import random

def main():
    balance = 2000
    print(f"\nStarting new game with ${balance}")
    deck = create_deck()
    game(balance, deck)

def create_deck():
    cards = ["Ace", "Jack", "Queen", "King", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    deck = []
    for card in cards:
        for _ in range(4):    #with a loop, we can put each card in the deck four times. Suit doesn't matter in blackjack
            deck.append(card)
    random.shuffle(deck)
    return deck

def game(balance, deck):
    player_points = 0                 #start game with no points
    dealer_points = 0

    while balance > 0:
        while True:
            try:
                player_blackjack = "False"
                dealer_blackjack = "False"
                print(f"Current balance: {balance}")
                bet = int(input("Enter the amount you'd like to bet: ").strip(" $").replace(",", ""))
                if bet <= 0 or bet > balance:
                    raise ValueError
                break
            except ValueError:
                print("Error: bet is out of bounds.")

        balance -= bet
        if len(deck) < 26:
                print("Shuffling deck...")
                deck = create_deck()
        print(f"\nYour cards: {deck[0]} and {deck[2]}")
        if deck[0] != "Ace" and deck[2] != "Ace":
            player_points = get_value(deck[0]) + get_value(deck[2])
            print(f"Total value: {player_points}")
        elif deck[0] == "Ace" and deck[2] != "Ace":
            player_points = get_value(deck[0])
            a,b = (player_points.split("/"))
            a = int(a)
            b = int(b)
            a += get_value(deck[2])
            b += get_value(deck[2])
            player_points = f"{a}/{b}"
            print(f"Total value: {player_points}")
        elif deck[0] != "Ace" and deck[2] == "Ace":
            player_points = get_value(deck[2])
            a,b = (player_points.split("/"))
            a = int(a)
            b = int(b)
            a += get_value(deck[0])
            b += get_value(deck[0])
            player_points = f"{a}/{b}"
            print(f"Total value: {player_points}")
        else:
            player_points = "2/12"               #two aces yields a score of 2 or 12
            print(f"Total value: {player_points}")
        if player_points == "11/21":             #if we get 11/21 at this point (from only 2 cards), it means we have a blackjack hand
            player_blackjack = "True"
        d_card1 = deck[1]
        d_card2 = deck[3]
        for _ in range(4):
            deck.pop(0)

        print(f"Dealer's card: {d_card1} and unknown.\nDealer's known value: {get_value(d_card1)}")
        if d_card1 != "Ace" and d_card2 != "Ace":
            dealer_points = get_value(d_card1) + get_value(d_card2)
        elif d_card1 == "Ace" and d_card2 != "Ace":
            dealer_points = get_value(d_card1)
            a,b = (dealer_points.split("/"))
            a = int(a)
            b = int(b)
            a += get_value(d_card2)
            b += get_value(d_card2)
            dealer_points = f"{a}/{b}"
        elif d_card1 != "Ace" and d_card2 == "Ace":
            dealer_points = get_value(d_card2)
            a,b = (dealer_points.split("/"))
            a = int(a)
            b = int(b)
            a += get_value(d_card1)
            b += get_value(d_card1)
            dealer_points = f"{a}/{b}"
        else:
            dealer_points = "2/12"     #two aces yields a score of 2 or 12

        if dealer_points == "11/21":             #if we get 11/21 at this point (from only 2 cards), it means we have a blackjack hand
            dealer_blackjack = "True"

        while (type(player_points) == int and player_points < 21) or (type(player_points) == str and player_points != "11/21"):
            try:
                choice = input("Hit or stand?: ").strip().lower()
                if choice == "hit":
                    draw = deck[0]
                    deck.pop(0)
                    draw_value = get_value(draw)
                    print(f"\nYou drew {draw}.")
                    if type(player_points) == int and draw != "Ace":
                        player_points += draw_value
                        print(f"Total value: {player_points}")
                    elif type(player_points) == int and draw == "Ace":
                        a,b = (draw_value.split("/"))
                        a = int(a)
                        b = int(b)
                        a += player_points
                        b += player_points
                        if b > 21:
                            player_points = a
                        else:
                            player_points = f"{a}/{b}"
                        print(f"Total value: {player_points}")
                    elif type(player_points) == str and draw != "Ace":
                        a,b = (player_points.split("/"))
                        a = int(a)
                        b = int(b)
                        a += get_value(draw)
                        b += get_value(draw)
                        if b > 21:
                            player_points = a
                        else:
                            player_points = f"{a}/{b}"
                        print(f"Total value: {player_points}")
                    elif type(player_points) == str and draw == "Ace":
                        a,b = (player_points.split("/"))
                        a = int(a)
                        b = int(b)
                        a += 1                          #only need to add 1 from 1/11. ex: 2/12 + 1/11 --> 2/12 + 1 or 2/12 + 11 --> 3/13 or 13/23. 23 is out of bounds and 13 is redundant.
                        b += 1
                        if b > 21:
                            player_points = a
                        else:
                            player_points = f"{a}/{b}"
                        print(f"Total value: {player_points}")
                    else:
                        pass
                elif choice == "stand":
                    break
            except ValueError:
                pass

        if type(player_points) == int and player_points > 21:
            print(f"Bust!\nDealer's cards were {d_card1} and {d_card2}. Dealer wins!\n")
            if balance == 0:
                    print("Game over!")
        else:
            print(f"\nDealer's second card is {d_card2} for a total of {dealer_points}.")
            if type(dealer_points) == str:
                a,b = dealer_points.split("/")
                a = int(a)
                b = int(b)
            while (type(dealer_points) == int and dealer_points <= 16) or (type(dealer_points) == str and b <= 17):         #dealer will hit on hard 16 or lower and soft 17 or lower
                print(f"Dealer hits.")
                draw = deck[0]
                deck.pop(0)
                draw_value = get_value(draw)
                print(f"\nDealer drew {draw}.")
                if type(dealer_points) == int and draw != "Ace":
                    dealer_points += draw_value
                    print(f"Dealer's total value: {dealer_points}")
                elif type(dealer_points) == int and draw == "Ace":
                    a,b = (draw_value.split("/"))
                    a = int(a)
                    b = int(b)
                    a += dealer_points
                    b += dealer_points
                    if b > 21:
                        dealer_points = a
                    else:
                        dealer_points = f"{a}/{b}"
                    print(f"Dealer's total value: {dealer_points}")
                elif type(dealer_points) == str and draw != "Ace":
                    a,b = (dealer_points.split("/"))
                    a = int(a)
                    b = int(b)
                    a += get_value(draw)
                    b += get_value(draw)
                    if b > 21:
                        dealer_points = a
                    else:
                        dealer_points = f"{a}/{b}"
                    print(f"Dealer's total value: {dealer_points}")
                elif type(dealer_points) == str and draw == "Ace":
                    a,b = (dealer_points.split("/"))
                    a = int(a)
                    b = int(b)
                    a += 1                          #only need to add 1 from 1/11. ex: 2/12 + 1/11 --> 2/12 + 1 or 2/12 + 11 --> 3/13 or 13/23. 23 is out of bounds and 13 is redundant.
                    b += 1
                    if b > 21:
                        dealer_points = a
                    else:
                        dealer_points = f"{a}/{b}"
                    print(f"Dealer's total value: {dealer_points}")
                else:
                    pass

            if player_blackjack == "True" and dealer_blackjack == "True":
                print("Push.\n")
                balance += bet
            elif player_blackjack == "True" and dealer_blackjack == "False":
                print("Blackjack! You win!\n")
                balance += (2.5*bet)                                                   #original bet is returned to balance and 1.5x payout is added
            elif player_blackjack == "False" and dealer_blackjack == "True":
                print("Dealer's Blackjack! You lose!\n")
            else:
                balance = check_winner(player_points, dealer_points, balance, bet)

                if balance == 0:
                    print("Game over!")
                elif balance > 1000000000:
                    print("You are a billionaire now. Casino's bankrupt :( ")
                    break
                else:
                    pass


def get_value(card):
    if card == "Jack" or card == "King" or card == "Queen":
        return 10
    elif card == "Ace":
        return "1/11"
    else:
        return card

def check_winner(player_points, dealer_points, balance, bet):
    if type(player_points) == str:
        a,b = player_points.split("/")
        b = int(b)
        player_points = b
    if type(dealer_points) == str:
        c,d = dealer_points.split("/")
        d = int(d)
        dealer_points = d
    if player_points == dealer_points:
        print("Push.\n")
        balance += bet
        return balance
    elif player_points < dealer_points and dealer_points <= 21:
        print("You lost!\n")
        return balance
    else:
        print("You win!\n")
        balance += (2*bet)
        return balance


if __name__ == "__main__":
    main()


