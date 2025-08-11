user_select = input("Would like to use miles or kilometers? (m/k): ").strip().lower()

if user_select == 'm':
    distance = float(input("Enter distance in miles: "))
    converted_distance_yards = distance * 1760
    converted_distance_feet = distance * 5280
    converted_distance_inches = distance * 63360
    print(f"Distance in yards: {converted_distance_yards}")
    print(f"Distance in feet: {converted_distance_feet}")
    print(f"Distance in inches: {converted_distance_inches}")
elif user_select == 'k':
    distance = float(input("Enter distance in kilometers: "))
    converted_distance_meters = distance * 1000
    converted_distance_centimeters = distance * 100000
    converted_distance_millimeters = distance * 1000000
    print(f"Distance in meters: {converted_distance_meters}")
    print(f"Distance in centimeters: {converted_distance_centimeters}")
    print(f"Distance in millimeters: {converted_distance_millimeters}")
else:
    print("Invalid selection. Please enter 'm' for miles or 'k' for kilometers.")