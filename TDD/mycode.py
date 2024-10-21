def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y
    # if "-" in str(x):
    #     x = 0 - x
    # elif "-" in str(y):
    #     y = 0 - x
    # return x - y

def divide(x, y):
    if x == 0 or y == 0:
        diff = "Invalid"
    else:
        diff = x / y
    return diff