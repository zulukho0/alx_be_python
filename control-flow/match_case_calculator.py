num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /):")
message = "The result is"
match operation:
    case "+":
        print("The result is", num1+num2)
    case "-":
        print("The result is", num1-num2)
    case "*":
        print("The result is", num1*num2)
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot devide by zero.")
        else:
            print("The result is", num1/num2)
    case _:
        print("Enter a valid number")

