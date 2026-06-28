import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
    sys.exit()

menu = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
    
    print(tabulate(menu, headers="keys", tablefmt="grid"))
    
except FileNotFoundError:
    sys.exit()