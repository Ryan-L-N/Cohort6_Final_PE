def convert_miles(miles):
    yards = miles * 1760
    feet = miles * 5280
    inches = miles * 63360
    return yards, feet, inches

def convert_kilometers(kilometers):
    meters = kilometers * 1000
    centimeters = kilometers * 100000
    millimeters = kilometers * 1000000
    return meters, centimeters, millimeters

def main():
    print("Choose a unit to input:")
    print("1. Miles above Mars")
    print("2. Kilometers above Mars")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        try:
            miles = float(input("Enter the number of miles above Mars: "))
            if miles < 0:
                print("Distance cannot be negative!")
                return
            yards, feet, inches = convert_miles(miles)
            print(f"\n{miles} miles above Mars equals:")
            print(f"{yards:,.2f} yards")
            print(f"{feet:,.2f} feet")
            print(f"{inches:,.2f} inches")
        except ValueError:
            print("Please enter a valid number!")
            
    elif choice == "2":
        try:
            kilometers = float(input("Enter the number of kilometers above Mars: "))
            if kilometers < 0:
                print("Distance cannot be negative!")
                return
            meters, centimeters, millimeters = convert_kilometers(kilometers)
            print(f"\n{kilometers} kilometers above Mars equals:")
            print(f"{meters:,.2f} meters")
            print(f"{centimeters:,.2f} centimeters")
            print(f"{millimeters:,.2f} millimeters")
        except ValueError:
            print("Please enter a valid number!")
            
    else:
        print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()