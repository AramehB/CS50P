# BLACKJACK IN PYTHON
    #### Video Demo:  https://youtu.be/GpHM_UpWv8E
    #### Description:
    This program implements a text-based version of the game Blackjack in Python - where you play against a dealer (computer).
    You start the game with a balance of $2000 and bet your way into becoming a billionaire!
    You are given a hand, and decide to hit(draw) or stand(stop drawing) until you get as close to 21 as possible.
    If either player or dealer goes over 21, they bust(lose).
    If your score is greater than the dealer's you win! If it is less, you lose! If the values are equivalent, play again!
    The game keeps going until you either run out of money or the casino goes bankrupt (hah, good luck!)
    Jacks, Queens, and Kings are worth 10 points, and the Ace has a value of 1/11.
    If the higher value of the Ace takes you over 21, the game will default you to the lower one so you don't bust.
    If you draw an Ace and a card equivalent to a value of 10 as your first two cards, that's a Blackjack hand!
        You win your bet money back, and additional winnings equal to 1.5x your initial bet!
        (unless the dealer also got blackjack, in which case you get nothing!!!)
        ex: if you have a balance of $2000 and you bet $1000 and get Blackjack, your new balance is $3500
    The dealer is programmed to hit on hard 16 or lower, and soft 17 ("7/17") or lower, just like in real life!

    When the amount of cards in the deck goes below 26 as a result of player and dealer draws, the program
    will automatically recreate the deck to make sure that the deck never runs out of cards

    One important thing to note is that if both players get a 21, but only one player gets a 21 as a Blackjack hand,
    that player will win the round by default - just like how the actual game is played. Be careful!
