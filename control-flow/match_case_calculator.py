num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Chooe the operation (+, -, *, /): ")
message = "The result is"
match operation:
    case "+":
        print(message, num1+num2)
    case "-":
        print(message, num1-num2)
    case "*":
        print(message, num1*num2)
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot devide by zero.")
        else:
            print(message, num1/num2)
    case _:
        print("Enter a valid number")

