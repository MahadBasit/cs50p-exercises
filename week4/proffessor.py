import random


def main():
    a = get_level()
    score = 0
    for _ in range(10):
        b = generate_integer(a)
        c = generate_integer(a)
        tries = 0
        while True:
            try:
                ans = int(input(f'{b}+{c} = '))
                tries += 1

                if ans == b+c:
                    score += 1
                    break

                elif tries == 3 and ans != b+c:
                    print(f'{b}+{c} = {b+c}')
                    break

                elif ans != b+c:
                    print("EEE")
                    
                
                
            except ValueError:
                tries += 1
                print("EEE")

                if tries == 3:
                    print(f'{b}+{c} = {b+c}')
                    break

    print(score)

                
                


def get_level():
    while True:
        try:
            n = int(input("Enter level: "))
            if n in (1,2,3):
                break
        except ValueError:
            pass
    return n
        


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)

    elif level == 2:
        x = random.randint(10,99)

    elif level == 3:
        x = random.randint(100,999)
        
    return x


if __name__ == "__main__":
    main()