def perform_operation(num1, num2, operation):
    operation = operation.lower()
    
    if operation == "add":
        return num1 +num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num1 == 0 or num2 == 0:
            message = "Cannot divide by 0"
            return message
        else:
            return num1 / num2