def main():
    while True:
        try:
            frac = input("Enter remaining fuel over total capacity as x/y: ")
            f = convert(frac)
            break
        except (ValueError, ZeroDivisionError, IndexError):
            pass

    print(gauge(f))

def convert(fraction):
    try:
        fraction = fraction.split("/")
        x = int(fraction[0]) 
        y = int(fraction[1])

        if y == 0:
            raise ZeroDivisionError

        if x >= 0 and y > 0 and x <= y:
            return round((x/y)*100)
        
        else:
            raise ValueError

    except (ValueError, IndexError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    
    elif percentage >= 99:
        return 'F'
    
    else: return f'{percentage}%'


if __name__ == "__main__":
    main()