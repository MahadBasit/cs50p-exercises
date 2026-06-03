def energy(m):
    c = 300000000
    return m*c*c

def main():
    mass = int(input("Enter a mass: "))
    energy_result = energy(mass)
    print(f"Energy = {energy_result}J")
main() 