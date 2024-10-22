# Calculator?

def calculator():
    num1 = int(input("Enter first number:\n"))
    num2 = int(input("Enter second number:\n"))
    operation = input("Choose:\n1)Add:\n2)Subtract:\n3)Multiply:\n4)Divide:\n")
    
    if operation == "1":
        add(num1,num2)

    elif operation == "2":
        subtract(num1,num2)
        

    elif operation == "3":
        multiply(num1,num2)
        
        
    elif operation == "4":
        divide(num1,num2)
        
    else:
        return "Please choose from 1-4"

def add(num1,num2):
    add = num1 + num2
    return add

def subtract(num1,num2):
    subtract = num1 - num2
    return subtract

def multiply(num1,num2):
    multiply = num1 * num2
    return multiply

def divide(num1,num2):
    if num2 == 0:
        return "Invalid"

    divide = num1 / num2
    
    return divide


# To not run the app but just the test even with user input, call if name stuff
if __name__ == "__main__":
    calculator()




    

    

# calculator()