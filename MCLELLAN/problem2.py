# SOLUTION PROBLEM 2:
# Pizza Efficiency (area per dough unit):
# Automatron 1 (2 circles): 17.67
# Automatron 2 (triangle): 8.66
# Automatron 3 (square): 18.00
# Best deal: Automatron 3 (square) with 18.00 area per dough unit!

import math

def area_circle(diameter):
	radius = diameter / 2
	return math.pi * radius ** 2

def area_equilateral_triangle(side):
	return (math.sqrt(3) / 4) * side ** 2

def area_square(side):
	return side ** 2

def efficiency(area, dough):
	return area / dough

# Automatron 1
circle_area = area_circle(15) * 2
circle_eff = efficiency(circle_area, 20)

# Automatron 2
triangle_area = area_equilateral_triangle(20)
triangle_eff = efficiency(triangle_area, 20)

# Automatron 3
square_area = area_square(18)
square_eff = efficiency(square_area, 18)

efficiencies = [
	("Automatron 1 (2 circles)", circle_eff),
	("Automatron 2 (triangle)", triangle_eff),
	("Automatron 3 (square)", square_eff)
]

best = max(efficiencies, key=lambda x: x[1])

print("Pizza Efficiency (area per dough unit):")
for name, eff in efficiencies:
	print(f"{name}: {eff:.2f}")
print(f"\nBest deal: {best[0]} with {best[1]:.2f} area per dough unit!")
