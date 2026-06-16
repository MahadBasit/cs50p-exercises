l1 = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in l1:
            l1[item] += 1
        else:
            l1[item] = 1
        
    except EOFError:
        break



for w, c in sorted(l1.items()):
    print(f'{c} {w.upper()}')