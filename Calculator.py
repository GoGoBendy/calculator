import sys

while True:
    print("What calculation would you like?")
    print("1. Addition")
    print("2. subtraction")
    print("3. division")
    print("4. multiplication")
    print("5. unit conversion")
    print("6. sort")
    gavlik = input("Enter number of calculation: ")
    unit = gavlik.lower()
    if unit == "6":
        numbers = list(input("Please input the numbers you want to sort "))
        numbers.sort()
        print(numbers)
    elif unit == "5":

        def inches_to_cm(inches):
            return inches * 2.54

        def cm_to_inches(cm):
            return cm / 2.54

        def feet_to_meters(feet):
            return feet * 0.3048

        def meters_to_feet(meters):
            return meters / 0.3048

        def main():
            print("Unit Conversion Program")
            print("1. Inches to Centimeters")
            print("2. Centimeters to Inches")
            print("3. Feet to Meters")
            print("4. Meters to Feet")
            print("5. Celsius to Fahrenheit")

        print(main())

        choice = int(input("Enter your conversion metrics: "))

        if choice == 1:
            inches = float(input("Enter length in inches: "))
            cm = inches_to_cm(inches)
            print(f"{inches} inches is equal to {cm:.2f} centimeters")
        elif choice == 2:
            cm = float(input("Enter length in centimeters: "))
            inches = cm_to_inches(cm)
            print(f"{cm} centimeters is equal to {inches:.2f} inches")
        elif choice == 3:
            feet = float(input("Enter length in feet: "))
            meters = feet_to_meters(feet)
            print(f"{feet} feet is equal to {meters:.2f} meters")
        elif choice == 4:
            meters = float(input("Enter length in meters: "))
            feet = meters_to_feet(meters)
            print(f"{meters} meters is equal to {feet:.2f} feet")
        elif choice == 5:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print(
                f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit"
            )
        else:
            print("Invalid choice")

    else:
        number1 = float(input("What's the first number you want to calculate?"))
        number2 = float(input("What's the second number you want to calculate?"))
        answer = 0
        if unit == "1":
            answer = number1 + number2
            print(answer)
        elif unit == "2":
            answer = number2 - number1
            print(answer)
        elif unit == "3":
            answer = number1 / number2
            print(answer)
        elif unit == "4":
            answer = number1 * number2
            print(answer)
        else:
            print("Error: input not recognised")

    print("Would you like to calculate again? (yes/no)")
    calculate = input()
    if calculate == "no":
        sys.exit()
