while True:
    try:
        X, Y = (input("Fraction: ").split("/"))

        X = int(X)
        Y = int(Y)

        if X > Y or Y == 0:
            raise ValueError

        result = round((int(X) / int(Y)) * 100)

        if 0 <= result <= 1:
            print("E")
            break
        elif result >= 99:
             print("F")
             break
        elif 1 < result < 99:
             print(str(result) + "%")
             break
        else:
            None

    except:
        ValueError or ZeroDivisionError
