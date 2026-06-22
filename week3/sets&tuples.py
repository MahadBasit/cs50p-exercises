'''
l = [1,2,2,3,4,4]

l = set(l)

print(l)


l1 = [1,2,3,4]
l2 = [2,3,4,5]

l1 = set(l1)
l2 = set(l2)

common = l1 & l2
print(list(common))


l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

dl = set(l1) - set(l2)

print(list(dl))


def main():
    
    l1 = [1,2,3,3,5]
    u = unique(l1)
    print(u)

def unique(m):
   if len(m) == len(set(m)):
       return True
   else:
       return False

main()


sen = "hello world"

count = len(set(sen) & set('aeiou'))

print(count)



l1 = [1,2,3,4]
l2 = [3,4,5,6]
l1 = set(l1)
l2 = set(l2)

l3 = l1^l2   #symmetric difference

print(list(l3))


lists = [[1,2,3], [2,3,4], [3,4,5]]

result = set(lists[0])
for i in lists[1:]:
    result &= set(i)

print(list(result))



l1 = [1,2,4,5,7,9]
m = (set(range(1,11))) - set(l1)
print(list(m))



math = {"alice", "bob", "charlie"}
science = {"bob", "charlie", "diana"}

s = math^science
print(s)



def main():
    numbers = [1,2,45,3,-76,88]
    t = stats(numbers)
    a, b, c = t
    print(a)
    print(b)
    print(c)

def stats(l):
    mx = l[0]
    mn = l[0]
    total = l[0]

    for i in l[1:]:
        if i > mx:
            mx = i
        elif i < mn:
            mn = i
        total += i

    average = total/len(l)

    return (mn, mx, average) 

main()



students = [("Ali", 78), ("Sara", 92), ("Zain", 85), ("Hira", 92), ("Omar", 67)]

stu = sorted(students, key = lambda x: (-x[1], x[0]))

print(stu)



l1 = [1,2,4,4,5]
l2 = [4,5,6,7,8]
l3 = []

for i in l1:
    if i not in l3 and i in l2:
        l3.append(i)

print(l3)

l1 = set(l1)
l2 = set(l2)

l3 = l1.intersection(l2)
print(list(l3))



sen = "programming is interesting"

count = len(set(sen) & set('aeiou'))

print(count)



cricket = {"Ali", "Sara", "Zain", "Hira"}
football = {"Sara", "Omar", "Zain", "Bilal"}
basketball = {"Zain", "Hira", "Bilal", "Ali"}

l3 = cricket & football & basketball

l4 = (cricket - basketball) - football

l5 = cricket.intersection(football)
l6 = football.intersection(basketball)
l7 = cricket.intersection(basketball)

l8 = l5 | l6 | l7
print(l3)
print(l4)
print(l8)



dic2 = {(2,3,4):'b'} #valid because tuples are immutable
try:
    dic1 = {[1,2,3]:'a'} #invalid because lists are mutable, cannot be hashed
except TypeError as e:
    print(e)
'''