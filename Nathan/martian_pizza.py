#Calculate the best deal for pizza dough to surface area ratio given options of two round 15 inch pizzas, one equalateral triangle pizza with a side length of 20 inches, and one square pizza with a side length of 18 inches.
import math

def calculate_area_circle(radius):
    return math.pi * (radius ** 2)
def calculate_area_square(side_length):
    return side_length ** 2
def calculate_area_triangle(side_length):
    return (math.sqrt(3) / 4) * (side_length ** 2)
def calculate_pizza_area():
    # Two round pizzas
    radius = 15 / 2
    area_round_pizzas = 2 * calculate_area_circle(radius)

    # One equilateral triangle pizza
    side_length_triangle = 20
    area_triangle_pizza = calculate_area_triangle(side_length_triangle)

    # One square pizza
    side_length_square = 18
    area_square_pizza = calculate_area_square(side_length_square)

    return area_round_pizzas, area_triangle_pizza, area_square_pizza 

area_round_pizzas, area_triangle_pizza, area_square_pizza = calculate_pizza_area()

print(f"Area of two round pizzas: {area_round_pizzas:.2f} square inches")
print(f"Area of one equilateral triangle pizza: {area_triangle_pizza:.2f} square inches")
print(f"Area of one square pizza: {area_square_pizza:.2f} square inches")

# Determine the best deal
best_deal = max(area_round_pizzas, area_triangle_pizza, area_square_pizza)
if best_deal == area_round_pizzas:
    print("The best deal is two round pizzas.")
elif best_deal == area_triangle_pizza:
    print("The best deal is one equilateral triangle pizza.")
else:
    print("The best deal is one square pizza.")