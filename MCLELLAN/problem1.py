# SOLUTION PROBLEM 1:

def main():
    print("Please make your choice between the following: 'Miles above Mars' or 'Kilometers above Mars'?")
    choice = input("Enter 'Miles' or 'Kilometers': ").strip().lower()

    if choice == 'miles':
        try:
            miles = float(input("Enter the number of miles above Mars: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        yards = miles * 1760
        feet = miles * 5280
        inches = miles * 63360
        print(f"{miles} miles above Mars is:")
        print(f"  {yards:.2f} yards")
        print(f"  {feet:.2f} feet")
        print(f"  {inches:.2f} inches")
    elif choice == 'kilometers':
        try:
            km = float(input("Enter the number of kilometers above Mars: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
        meters = km * 1000
        centimeters = km * 100000
        millimeters = km * 1000000
        print(f"{km} kilometers above Mars is:")
        print(f"  {meters:.2f} meters")
        print(f"  {centimeters:.2f} centimeters")
        print(f"  {millimeters:.2f} millimeters")
    else:
        print("Invalid choice. Please enter 'Miles' or 'Kilometers'.")

if __name__ == "__main__":
    main()