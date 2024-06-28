def convert(str):
    print(str.replace(":)", "🙂").replace(":(", "🙁"))


def main():
    message = input("What would you like to say?: ")
    convert(message)

main()
