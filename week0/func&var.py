'''#Ask user's name, strip whitespaces along with capatalizing each word.
name = input("What's your name? ").strip().title()

#Split name into first and last name
first, last = name.split(" ")

#Say hello to user
print("hello,", name)
print("hello, ", end = "")
print(name)
print("hello,", name, sep= '???')
print(f'hello, {name}')
print(f'hello, {first}')
print(f'hello, {last}')
'''

#Calculator.py

'''
x = float(input())
y = float(input())
#z = round(x/y, 2)
z = x/y

print(f'{z:.2f}')

'''

#Functions
'''

def main():
    name = input("What's your name: ")
    hello(name)


def hello(to = "world"):
    print("hello,", to)


main()

'''

'''
def main():
    x = int(input("What's x? "))
    print("x squared is: ", square(x))

def square(n):
    return n*n  #n**2 or pow(n,2) --> these also do the same thing

main()
'''


def main():
    house = area(50,34)
    lawn = area(40,56)
    total = house + lawn
    print(total, "square feet")

def area(l,w):
    return l*w


main()