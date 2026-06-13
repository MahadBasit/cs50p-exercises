total = 0
count = 0

while True:
    n = input("Enter a number: ")
    if n == "done":
        break
    else:
        n = int(n)
        total += n
        count += 1
        print(f"Running total: {total}")

print(f"Final Sum: {total}")
print(f"Total numbers you entered: {count}")