exp = input("Enter any arithmetic expression : ").strip()
exp = exp.split()

x = float(exp[0])
y = exp[1]
z = float(exp[2])

if y == "+":
    print(f"{x + z:.1f}")

elif y == "-":
    print(f"{x - z:.1f}")

elif y == "*":
    print(f"{x*z:.1f}")

elif y == "/":
    print(f"{x/z:.1f}")
    
else:
    print("Invalid Expression")
         
