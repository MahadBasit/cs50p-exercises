while True:    
    try:
        frac = input("Enter remaining fuel over total capacity as x/y: ")
        frac = frac.split("/")
        x = int(frac[0]) 
        y = int(frac[1])
        if x >= 0 and y > 0 and x <= y:
            break

    except (ValueError, ZeroDivisionError, IndexError):
        pass

fuel = x/y

if fuel*100 <= 1:
    print('E')

elif fuel*100 >= 99:
    print('F')

else:
    print(f'{fuel*100:.0f}%')