def dateConvert(x,y,z):
    print(f"{int(z):04}-{int(x):02}-{int(y):02}")  #z, the year, has 4 places

def main():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if date[0].isalpha() and date.find("/") == -1 and date.find(",") != -1:
                x, y, z = date.split(" ")

                if x in months:
                    x = str((months.index(x)) + 1)
                else:
                    print("Error: month does not exist")
                    return

                y = y.rstrip(",")
                if 1 <= int(y) <= 31:
                    dateConvert(x, y, z)
                    break
                else:
                    print("Error: day does not exist")
                    continue

            else:
                x, y, z = date.split("/")
                if 1 <= int(x) <= 12 and 1 <= int(y) <= 31:
                    dateConvert(x, y, z)
                    break
                else:
                    ValueError

        except ValueError:
            print("Invalid format, try again.")
            continue



main()
