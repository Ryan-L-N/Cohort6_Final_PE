import os

def choose_mi_or_km() -> str:
    while True:
        choice = input("Would you like to use \"Miles\" or \"Kilometers\" above Mars: ").capitalize()
        if choice in ["Miles", "Kilometers"]:
            print("Accepted")
            return choice
        else:
            print("Invalid choice. Please enter \"Miles above Mars\" or \"Kilometers above Mars\".")


def apply_mi_or_km(choice: str) -> str:
    if choice == "Miles":
        #print("Miles")
        return Miles_Above_Mars()
    elif choice == "Kilometers":
        #print("KM")
        return KM_Above_Mars()

def Miles_Above_Mars() -> str:
    try:
        total_miles = float(input("How many miles?: "))
        #return total_miles
    except ValueError:
        print("Please put in a float")
    total_yards = 1760/total_miles
    print(f"The total number of yards is: " + str(total_yards))
    total_feet = 5280/total_miles
    print("The total number of feet is: " + str(total_feet))
    total_inches = 63380/total_miles
    print("The total number of inches is: " + str(total_inches))

def KM_Above_Mars() -> str:
    try:
        total_KM = float(input("How many kilometers?: "))
    except ValueError:
        print("Please put in a float")
    total_meters = 1000*total_KM
    print("The total number of meters is: " + str(total_meters))
    total_cm = 100000*total_KM
    print("The total number of centimeters is: " + str(total_cm))
    total_mm = 1000000*total_KM
    print("The total number of milimeters is: " + str(total_mm))

def main():
    print("Welcome")   
    choice = ""
    while not choice:
        choice = choose_mi_or_km()
    apply_mi_or_km(choice)
    
    
if __name__ == "__main__":
    main()
