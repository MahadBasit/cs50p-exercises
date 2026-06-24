import random

while True:
    try:
        n = int(input("Enter a level: "))
        if n > 0:
            break

    except ValueError:
        pass

a = random.randint(1,n)

while True:
    try:
        guess = int(input("Guess the number: "))
        if guess > 0:
            if guess < a:
                print('Too small!')
            elif guess > a:
                print('Too Large!')
            else:
                print('Just right!')
                break
                
    except ValueError:
        pass
 