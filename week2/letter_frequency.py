s = input("Enter a word: ")

current_char = s[0]
count = 1

for c in s[1:]:
    if c == current_char:
        count += 1

    else:
        print(current_char,count, sep = '',end = '')
        current_char = c
        count = 1

print(current_char, count, sep = '', end = '')
