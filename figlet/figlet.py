import sys
import random
from pyfiglet import Figlet


figlet = Figlet()

if len(sys.argv) == 1:                        #python figlet.py :file name is 1 argument
    msg = input("Input: ").strip()
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(figlet.renderText(msg))

elif len(sys.argv) == 3:                      #python figlet.py --font fontname :   fontname is 3rd argument
    if sys.argv[2] in figlet.getFonts() and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        msg = input("Input: ").strip()
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(msg))
    else:
        sys.exit("Error: One or more arguments are not valid")

else:
    sys.exit("Error: bad number of arguments")
