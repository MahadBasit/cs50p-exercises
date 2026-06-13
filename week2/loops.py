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



animals = ['lion', 'tiger', 'monkey', 'elephant']

fanimals = []

for animal in animals:
    fanimals.append(animal.title())    

fanimals = [animal.title() for animal in animals]

print(fanimals)

list = [1,2,3,4,5]
list.extend([[6,7,8]])
print(list)

fruits = ['apple', 'mango', 'pear']
capitalized = []
for fruit in fruits:
    capitalized.append(fruit.title())

capitalized = [fruit.title() for fruit in fruits]



list0 = [1, 3, 2, 1, 5, 3]
dup_list = []

for i in list0:
    if i not in dup_list:
        dup_list.append(i)
    

print(dup_list)


list1 = [9, 1, 2, 3, 4, 7]
max_num = list1[0]

for i in list1[1:]:
    if i > max_num:
        max_num = i

list1.remove(max_num)

max_num = list1[0]
for i in list1[1:]:
    if i > max_num:
        max_num = i

print(max_num)



dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
dict2 = {}

for w,c in dict1.items():
    dict2[c] = w


print(dict2)


ani = ['cat', 'dog', 'elephant', 'ant', 'bear']
dict1 = {}

for i in ani:
    n = len(i)
    if n in dict1:
        dict1[n].append(i)
    else:
        dict1[n] = [i]

print(dict1)


l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
l3 = []

for i in l1:
    for j in l2:
        if j == i:
            l3.append(j)
            break

print(l3)


w1 = input("Enter a word: ").lower()
w2 = input("Enter another word: ").lower()

l1 = sorted(w1)
l2 = sorted(w2)

if l1 == l2:
    print("Anagram")
else:
    print('Not an anagram')


stu = {'Ali' : 80, 'Sara' : 92, 'Hamza' : 67, 'Zara' : 88}
total = 0

for i in stu:
    total += stu[i]

avg = total/len(stu)

for j in stu:
    if stu[j] > avg:
        print(j)
'''