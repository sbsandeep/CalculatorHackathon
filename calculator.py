"""
The following code is what we should create and then test to make a 
functioning calculator.
"""
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    print("Error, this division is unable to occur due to a value of 0 allowed")
    return None
  return num1 / num2
def exponent(num1, num2):
    return num1 ** num2

def modulo(num1, num2):
    if num2 == 0:
        print("Error: Modulo by zero is not allowed")
        return None
    return num1 % num2
 

print("Addition:", add(5, 3))        
print("Subtraction:", subtract(8, 2))  
print("Multiplication:", multiply(4, 7))  
print("Division:", divide(10, 2))    
print("Division:", divide(10, 0))  

def calculate():
    num1 = float(input("Enter first value: "))
    operator = input("Enter operator [+,-,*,/]: ")
    num2 = float(input("Enter second value: "))
    result = None

    if operator == "+":
        result = add(num1, num2)
    elif operator == "-":
        result = subtract(num1, num2)
    elif operator == "*":
        result = multiply(num1, num2)
    elif operator == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operator")
        return result
    
    return result

while True:
    print("Result:", calculate())
    repeat = input("Do you want to repeat this process? (Yes/No): ")
    if repeat.lower() != "yes":
        print("Thank you for using this calculator.")
        break
 
 
    
      
    
  