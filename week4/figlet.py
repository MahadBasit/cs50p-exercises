import sys
import random
from pyfiglet import Figlet

s = input("Enter a sentence: ")

figlet = Figlet()
lof = figlet.getFonts()
rf = random.choice(lof)

if len(sys.argv) == 1:
    figlet.setFont(font = rf)
    print(figlet.renderText(s))

elif len(sys.argv) == 3 :
    if sys.argv[2] not in lof or (sys.argv[1] != '-f' and sys.argv[1] != '--font'):
        sys.exit('Wrong Input!')
    else:    
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(s))

else:
    sys.exit("Invalid number of arguments")