'''
i = 0

while i < 3:
    print("meow")
    i += 1 

for _ in range(3):
    print("meow")


print("meow\n" * 3, end = '')


while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(n):
    for _ in range(n):
        print("meow")
main()



students = ["Hermione", "Ron", "Harry"]

for i in range(len(students)):
    print(i+1, students[i])



students = {"Hermione" : "Gryffindor", 
            "Harry" : "Gryffindor",
            "Draco" : "Slytherin"
            }

for s in students:
    print(s, students[], sep = ': ')


    
students =[
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ": ")

    

def main():
    col(3)

def col(height):
    for _ in range(height):
        print("#")

main()
'''
