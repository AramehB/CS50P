import sys

if len(sys.argv) == 2:
    if (sys.argv[1]).endswith(".py"):
        try:
            x = sys.argv[1]
            with open(f"{x}", "r") as file:
                number_of_lines = 0
                for line in file:
                    if line.strip() != "" and not line.strip().startswith("#"):            # if line != "" doesnt work, must be line.strip() != "" because whitespace doesn't count as empty string
                        number_of_lines += 1
                print(number_of_lines)

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a python file.")
else:
    sys.exit("Incorrect number of command-line arguments.")
