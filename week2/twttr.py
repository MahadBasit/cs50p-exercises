text = input("Input: ")

result = ""

for char in text:
    if char not in ["a","e","i","o","u","A","E","I","O","U"]:
        result = result + char

print(f"Output: {result}")