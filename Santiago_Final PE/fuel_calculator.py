import math

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

def main():
    total_fuel = 0
    try:
        with open('module_masses.txt', 'r') as file:
            masses = [int(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print("module_masses.txt not found. Please enter module masses manually (one per line, enter empty line to finish):")
        masses = []
        while True:
            mass = input()
            if mass == "":
                break
            try:
                masses.append(int(mass))
            except ValueError:
                print("Invalid input, please enter a number.")
    
    for mass in masses:
        if mass < 0:
            print(f"Skipping negative mass: {mass}")
            continue
        fuel = calculate_fuel(mass)
        if fuel > 0:
            total_fuel += fuel
        else:
            print(f"Mass {mass} requires no fuel (fuel calculated as {fuel})")
    
    print(f"Total fuel required: {total_fuel}")

if __name__ == "__main__":
    main()