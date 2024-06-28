import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s = s.strip()

    match = re.search(r"^(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)\s{1}to\s{1}(1[0-2]|[1-9]):?([0-5][0-9])?\s(AM|PM)$", s)
    if match:
        times = match.groups()
        #example: ('7', '00', 'PM', '9', '00', 'AM')
        first_hour = times[0]
        first_minutes = times[1]
        second_hour = times[3]
        second_minutes = times[4]

        if first_minutes == None:
            first_minutes = "00"
        if second_minutes == None:
            second_minutes = "00"


        if first_hour == "12" and times[2] == "AM":
            first_hour = "00"
        elif times[0] != "12" and times[2] == "PM":
            first_hour = str(int(first_hour) + 12)
        else:
            None

        if second_hour == "12" and times[5] == "AM":
            second_hour = "00"
        elif times[3] != "12" and times[5] == "PM":
            second_hour = str(int(second_hour) + 12)
        else:
            None

        converted_time = f"{int(first_hour):02}:{first_minutes} to {int(second_hour):02}:{second_minutes}"          #must convert to int before we can prefix missing zeroes
        return converted_time

    else:
        raise ValueError("Error: No match found. Perhaps check formatting.")




if __name__ == "__main__":
    main()
