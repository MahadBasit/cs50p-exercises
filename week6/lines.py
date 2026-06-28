import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith('.py'):
    sys.exit()

count = 0
try:
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        for line in lines:
            if line.lstrip().startswith("#") or len(line.strip()) == 0:
                continue
            else:
                count += 1

    print(count)

except FileNotFoundError:
    sys.exit()