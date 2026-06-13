txt = input("Enter a word: ").lower()

ntext = txt[::-1]

if ntext == txt:
    print("Palindrome")

else:
    print("Not Palindrome")
    