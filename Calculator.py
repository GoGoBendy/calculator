while True == True:
    gavlik = input("What calculation would you like? (Addition, subtraction, division, multiplication, sort) ")
    unit = gavlik.lower()
    if unit == "sort":
        numbers = list(input("Please input the numbers you want to sort "))
        numbers.sort()
        print(numbers)
    else:
        number1 = float(input("What's the first number you want to calculate?"))
        number2 = float(input("What's the second number you want to calculate?"))
        answer = 0
        if unit == "addition":
            answer = number1+number2
            print(answer)
        elif unit == "subtraction":
            answer = number2-number1
            print(answer)
        elif unit == "division":
            answer = number1/number2
            print(answer)
        elif unit == "multiplication":
            answer = number1*number2
            print(answer)
        else:
            print("Error: input not recognised")