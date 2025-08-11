#Fuel required to launch a given module is based on its mass
import math

try:
    with open("Fuel_Module_Mass.txt", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path and try again.")

module_masses = content.splitlines()
fuel_requirements = [] 
for mass in module_masses:
    try:
        mass = int(mass.strip())
        fuel = math.floor(mass / 3) - 2
        fuel_requirements.append(fuel)
    except ValueError:
        print(f"Invalid mass value: {mass}. Please ensure all values are integers.")


total_fuel = sum(fuel_requirements)
print(f"Total fuel required for all modules: {total_fuel} units")