import sys
import csv

students = []
if len(sys.argv) == 3:
    if (sys.argv[1]).endswith(".csv") and (sys.argv[2]).endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    students.append({"first": first, "last": last, "house": house})
        except FileNotFoundError:
            sys.exit("Error: The file was not found.")
    else:
        sys.exit("Error: One or more of the files is not a CSV file.")
elif len(sys.argv) <= 3:
    sys.exit("Error: Too few command-line arguments.")
else:
    sys.exit("Error: Too many command-line arguments.")


try:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writeheader()                                                                                    #makes the first row the header: first,last,house
        for student in students:
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})
except FileNotFoundError:
    sys.exit("Error: The file was not found.")
