import math
from scipy.optimize import fsolve

# Mathematical operations
def add(*args):
    result = sum(args)
    explanation = f"Step 1: Addition: {args} = {result}"
    return result, explanation

def subtract(*args):
    result = args[0] - sum(args[1:])
    explanation = f"Step 1: Subtraction: {args} = {result}"
    return result, explanation

def multiply(*args):
    result = math.prod(args)
    explanation = f"Step 1: Multiplication: {args} = {result}"
    return result, explanation

def divide(*args):
    if 0 in args[1:]:
        raise ZeroDivisionError("Division by zero is not allowed.")

    result = args[0] / math.prod(args[1:])
    explanation = f"Step 1: Division: {args} = {result}"
    return result, explanation

def power(*args):
    result = args[0] ** args[1]
    explanation = f"Step 1: Exponentiation: {args} = {result}"
    return result, explanation

def square_root(*args):
    result = math.sqrt(args[0])
    explanation = f"Step 1: Square Root: √{args[0]} = {result}"
    return result, explanation

def logarithm(*args):
    result = math.log(args[0], args[1])
    explanation = f"Step 1: Logarithm: log{args[1]}({args[0]}) = {result}"
    return result, explanation

# Equation solver
def solve_equation(*args):
    equation = args[0]
    variable = args[1]
    equation = equation.replace(variable, "-(" + variable + ")")  # Convert to f(x) = 0 form
    equation_func = lambda x: eval(equation)
    solution = fsolve(equation_func, 0)
    explanation = f"Step 1: Solving Equation: {equation} = 0\nStep 2: Solution: {variable} = {solution[0]}"
    return solution[0], explanation

# Main calculator function
def scientific_calculator():
    print("Scientific Calculator")
    print("---------------------")

    operations = {
        "1": ("add", "Addition", "Addition operation adds two or more numbers together."),
        "2": ("subtract", "Subtraction", "Subtraction operation subtracts one or more numbers from the first number."),
        "3": ("multiply", "Multiplication", "Multiplication operation multiplies two or more numbers together."),
        "4": ("divide", "Division", "Division operation divides the first number by one or more numbers."),
        "5": ("power", "Exponentiation", "Exponentiation operation raises the first number to the power of the second number."),
        "6": ("square_root", "Square Root", "Square Root operation calculates the square root of a number."),
        "7": ("logarithm", "Logarithm", "Logarithm operation calculates the logarithm of a number with a specified base."),
        "8": ("solve_equation", "Solve Equation", "Solve Equation operation finds the solution to a given equation with a specified variable."),
    }

    result = None
    explanation = None

    while True:
        if result is not None:
            print(f"\nCurrent Result: {result}\n")

        print("Select an operation:")
        for key, (_, operation_name, operation_description) in operations.items():
            print(f"{key}. {operation_name}: {operation_description}")

        choice = input("Enter your choice (or 'exit' to quit): ")

        if choice == "exit":
            break

        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        operation_func, operation_name, _ = operations[choice]

        try:
            print(f"\nOperation: {operation_name}")
            num_args = int(input("Enter the number of arguments: "))
            args = []
            for i in range(num_args):
                args.append(float(input(f"Enter argument {i+1}: ")))

            result, explanation = eval(operation_func)(*args)
            print("\nStep-by-step Explanation:")
            print(explanation)

            while True:
                print("\nSelect an option:")
                print("1. Redo Last Step")
                print("2. Return to Main Menu")
                print("3. Combine with Another Operation")

                option = input("Enter your choice: ")

                if option == "1":
                    if result is not None and explanation is not None:
                        print("\nRedoing Last Step...")
                        print("\nStep-by-step Explanation:")
                        print(explanation)
                        print(f"Current Result: {result}")
                    else:
                        print("No previous step to redo.")

                elif option == "2":
                    result = None
                    explanation = None
                    break

                elif option == "3":
                    print("\nSelect another operation to combine:")
                    for key, (_, operation_name, operation_description) in operations.items():
                        print(f"{key}. {operation_name}: {operation_description}")

                    sub_choice = input("Enter your choice: ")

                    if sub_choice not in operations:
                        print("Invalid choice. Please try again.")
                        continue

                    sub_operation_func, sub_operation_name, _ = operations[sub_choice]

                    num_args = int(input("Enter the number of arguments: "))
                    args = []
                    for i in range(num_args):
                        args.append(float(input(f"Enter argument {i+1}: ")))

                    sub_result, sub_explanation = eval(sub_operation_func)(*args)
                    print("\nStep-by-step Explanation:")
                    print(sub_explanation)

                    result = sub_result
                    explanation += "\n" + sub_explanation

                else:
                    print("Invalid option. Please try again.")

        except ValueError as e:
            print(f"Error: {str(e)}")
        except ZeroDivisionError as e:
            print(f"Error: {str(e)}")

    print("Calculator exited.")

scientific_calculator()
