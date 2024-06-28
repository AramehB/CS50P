import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 2:
    if (sys.argv[1]).endswith(".csv"):
        pizza = []
        try:
            x = sys.argv[1]
            with open(f"{x}") as file:
                reader = csv.reader(file)
                for row in reader:
                    pizza.append({"pizza": row[0], "small": row[1], "large": row[2]})

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a csv file.")

elif len(sys.argv) >= 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")

print(tabulate(pizza, headers = "firstrow", tablefmt="grid"))
