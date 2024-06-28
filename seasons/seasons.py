from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    try:
        Y,M,D = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    words = (p.number_to_words(get_days_old(Y,M,D)*24*60) + " minutes").replace(" and", "").capitalize()    #get days as minutes, no "and" in the sentence
    print(words)




def get_days_old(Y,M,D):
    try:
        DOB = date(int(Y), int(M), int(D))                    #automatically checks if date is valid. otherwise error. ie 1999 02 29 is error since 1999 is not leap year
    except ValueError:
        sys.exit("Invalid Date")
    current_date = date.today()
    delta = (current_date - DOB)                          #gives days and time
    days_old = delta.days
    return days_old


if __name__ == "__main__":
    main()


