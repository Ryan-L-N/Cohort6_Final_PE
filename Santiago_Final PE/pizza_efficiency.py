import math

def calculate_circle_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def calculate_triangle_area(side):
    return (math.sqrt(3) / 4) * side ** 2

def calculate_square_area(side):
    return side ** 2

def main():
    area1 = 2 * calculate_circle_area(15)
    efficiency1 = area1 / 20
    area2 = calculate_triangle_area(20)
    efficiency2 = area2 / 20
    area3 = calculate_square_area(18)
    efficiency3 = area3 / 18
    
    print("Efficiencies (area per unit dough):")
    print(f"First Automatron: {efficiency1:.2f} sq inches per unit")
    print(f"Second Automatron: {efficiency2:.2f} sq inches per unit")
    print(f"Third Automatron: {efficiency3:.2f} sq inches per unit")
    
    efficiencies = {
        "First": efficiency1,
        "Second": efficiency2,
        "Third": efficiency3
    }
    
    best = max(efficiencies, key=efficiencies.get)
    print(f"\nThe most efficient Automatron is the {best} one.")

if __name__ == "__main__":
    main()