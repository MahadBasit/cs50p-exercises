import sys
import csv

if len(sys.argv) != 3:
    sys.exit()

hogwarts = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for line in reader:
            hogwarts.append(line)    
 
    with open(sys.argv[2], 'w', newline='') as file:
        
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()

        for i in hogwarts:
            last_name, first_name = i['name'].split(', ') 
            writer.writerow({'first': first_name, 'last': last_name, 'house': i['house']})


except FileNotFoundError:
    sys.exit()