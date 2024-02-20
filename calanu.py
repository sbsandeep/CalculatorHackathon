import math
 
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponent(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    return num1 % num2

def squareroot(num1, num2=None):
    if num1 < 0:
        print("Error: Cannot calculate square root of a negative number for num1!")
        return None
    if num2 is not None and num2 < 0:
        print("Error: Cannot calculate square root of a negative number for num2!")
        return None

    sqrt1rslt = math.sqrt(num1)
    if num2 is not None:
        sqrt2reslt = math.sqrt(num2)
        return sqrt1rslt, sqrt2reslt
    else:
        return sqrt1rslt

previous_answer = None

print("Selection operator")
while True:
    # Take input from the user
    
   # print("pi value is",math.pi)
    #print("ceil value is", math.ceil(1.89))
    #print("Floor value is", math.floor(6.69))
    
    operator = input("Enter operator (+, -, *, /, **, %, ^): ")

    if operator in ('+', '-', '*', '/', '**', '%', '^'):
        try:
            if previous_answer is None:
                num1 = float(input("Enter first number: "))
            else:
                num1 = previous_answer  # Use previous answer as the first number                 

            num2 = float(input("Enter second number: "))
            if num2 == 0:
                if operator == '/':
                    print("Error, this division is unable to occur due to a value of 0 allowed")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if operator == '+':
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
        elif operator == '-':
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)
        elif operator == '*':
            result = multiply(num1, num2)
            print(num1, "*", num2, "=", result)
        elif operator == '/':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
        elif operator == '**':
            result = exponent(num1, num2)
            print(num1, "**", num2, "=", result)
        elif operator == '%':
            result = modulo(num1, num2)
            print(num1, "%", num2, "=", result)
        elif operator == '^':
            if num2 is None:
                result = squareroot(num1)
                print(f"Square root of {num1} is", result)
            else:
                result, result2 = squareroot(num1, num2)
                print(f"Square root of {num1} is", result)
                print(f"Square root of {num2} is", result2)

        previous_answer = result

    else:
        print("enter a valid Operator [+, -, *, /, **, %, ^]")

    next_calculation = input("Let's do the next calculation? (yes/no): ")
    while True:
        if next_calculation == "no":
            break
        elif next_calculation == "yes":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            next_calculation = input("Let's do the next calculation? (yes/no): ")

    if next_calculation == "no":
        print("Exiting the program.")
        break
