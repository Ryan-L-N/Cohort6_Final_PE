# SOLUTION PROBLEM 3:
# Total fuel required: 3332538

def fuel_required(mass):
	return mass // 3 - 2

def total_fuel_from_file(filename):
	total = 0
	with open(filename) as f:
		for line in f:
			line = line.strip()
			if line:
				mass = int(line)
				total += fuel_required(mass)
	return total

if __name__ == "__main__":
	filename = "input.txt"
	total_fuel = total_fuel_from_file(filename)
	print(f"Total fuel required: {total_fuel}")
