sen = input("Enter a sentence: ").lower().split()

freq = {}

for w in sen:
    freq[w] = freq.get(w,0) + 1

for w, c in freq.items():
    print(w,":",c)