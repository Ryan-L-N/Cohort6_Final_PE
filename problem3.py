import math
mass=[]
with open ("masses.txt", "r") as file: 
    for i in file: 
        
        mass.append(int(i.strip()))

total_fuel=0

for i in mass:
    i=int(i)
    floor=math.floor(i/3)
    fuel_needed= floor-2 
    total_fuel += fuel_needed

print (total_fuel)
