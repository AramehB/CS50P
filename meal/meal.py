def main():
    t = input("What time is it? ")
    new_time = convert(t)

    if 7.0 <= new_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= new_time <= 13.0:
        print("lunch time")
    elif 18.0 <= new_time <= 19.0:
        print("dinner time")
    else:
        None


def convert(time):
    x, y = time.strip().split(":")
    x = float(x)
    y = float(y) / 60

    return x + y


if __name__ == "__main__":
    main()
