def main():
    while True:
        try:
            user_input = input("Fraction: ")
            print(gauge(convert(user_input)))
            break

        except ValueError or ZeroDivisionError:
            None




def convert(fraction):
    X, Y = fraction.split("/")
    X = int(X)
    Y = int(Y)

    if X > Y:
        raise ValueError
    elif Y == 0:
        raise ZeroDivisionError
    else:
        result = round((int(X) / int(Y)) * 100)
        return result


def gauge(percentage):
    if 0 <= percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    elif 1 < percentage < 99:
        return (str(percentage) + "%")
    else:
        None


if __name__ == "__main__":
    main()
