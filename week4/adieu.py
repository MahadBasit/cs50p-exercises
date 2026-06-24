import inflect
p = inflect.engine()

nl = []

while True:
    try:
        name = input('Name: ')
        nl.append(name)
    except EOFError:
        break

s = 'Adieu, adieu, to '
a = p.join(nl)

print(s+a)