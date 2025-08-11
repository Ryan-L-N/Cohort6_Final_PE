import math

def area_circle(diameter):
    circle_pizza_area = 2 * (math.pi * (diameter / 2) ** 2)
    return circle_pizza_area

def area_eq(length):
    eq_tri_pizza = (math.sqrt(3) / 4) * length ** 2
    return eq_tri_pizza

def area_sq(side):
    sq_pizza = side ** 2
    return sq_pizza


def automatron_eff(area, units):
    eff = area / units
    return eff

automatron1_eff = automatron_eff(area_circle(15), 20)
automatron2_eff = automatron_eff(area_eq(20), 20)
automatron3_eff = automatron_eff(area_sq(18), 18)

most_eff = automatron1_eff
best_auto = "Automatron 1"

if most_eff < automatron2_eff:
    most_eff = automatron2_eff
    best_auto = "Automatron 2"
if most_eff < automatron3_eff:
    most_eff = automatron3_eff
    best_auto = "Automatron 3"
    

print(f'The most efficient automatron is {best_auto} with {most_eff:.3f} area per dough units')

