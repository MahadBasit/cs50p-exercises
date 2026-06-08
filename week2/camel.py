variable = input("camelCase: ")

result = ""

for char in variable:
    if char.isupper():
        result = result + "_" + char.lower()
    else:
        result = result + char

print(f"snake_case: {result}")