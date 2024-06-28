import random

while True:                                       #true is always true, infinite loop
    try:
        n = int(input("Level: "))
        if 0 <= n:
            num = random.randint(1, n)            #NUMBER TO GUESS
            break                                 #breaks you out of loops, not conditionals
        else:
            raise ValueError

    except ValueError:
        None

while True:
    try:
        guess = int(input("Guess: "))            #USER'S GUESS
        if 0 <= guess:
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            raise ValueError
    except ValueError:
        None
