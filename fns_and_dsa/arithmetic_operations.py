def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide)").strip().lower()
    match operation :
        case  'add' :
            print(f"Result: {(num1 + num2)}")
        case 'subtract' :
            print(f"Result: {(num1 - num2)}")
        case 'multiply' :
            print(f"Result: {(num1 * num2)}")
        case 'divide' :
            if num1 > 0 and num2 > 0:
                print(f"Result: {(num1 / num2):.0f}")
            else :
                print("Cannot divide by zero.")


perform_operation()