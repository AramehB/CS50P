import random


def main():
    problem_number = 0
    score = 0
    level = get_level()
    while problem_number != 10:
        score += generate_integer(level)
        problem_number += 1
    print("Score:", score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:                 # a better way of my original "n == 1 or n == 2 or n == 3"
                return n

            else:
                raise ValueError

        except ValueError:
            None



def generate_integer(level):
    if level in [2, 3]:
        a = int("1" + (level-1)*"0")              #lower bound of range : 10? 100? 1000?...
        b = int("9" + (level-1)*"9")              #upper bound of range : 99? 999? 9999?...

    else:                                           #if only one digit numbers, the range is:
        a = 0
        b = 9                                      #0 to 9

    X = random.randint(a,b)
    Y = random.randint(a,b)

    #a better way would just be to do  ... if level 1, random.randint(0, 9) if level 2, random.randint(10, 99)

    attempt = 0                                 #attempts made on a particular problem
    while True:
        try:
            ans = int(input(f"{X} + {Y} = "))
            if ans == "":
                raise ValueError
            elif ans != X + Y:
                while attempt < 3:
                    print("EEE")
                    attempt += 1
                    break
                if attempt >= 3:                  #if we make 3 or more wrong attempts, just print out the correct ans and move on
                    print("X + Y =", X + Y)
                    return 0


            else:
                return 1
        except ValueError:
            None



if __name__ == "__main__":
    main()
