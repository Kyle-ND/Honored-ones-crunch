#import math 
#first_num = int(input("Enter first number: "))
#second_num = int(input("Enter second number: "))
#operator = input("Enter operator: ")

#operators=["+","-","/","*"]

#add = (first_num + second_num)    
#multiply = (first_num * second_num)   
#subtract = (first_num - second_num)  
#divide = (first_num / second_num)
    
#def calculator():
    #for operator in operators:

        #if operator == "+" :
            #print(add)

        #elif operators == "*":
         #print(multiply)
    
        #elif operator == "-":
           #print(subtract)
        #else:
           #print(divide)

#calculator()

def add(s,m):
    return s+m

def multiply(s,m):
    return s*m

def subtract(s,m):
    return s-m

def divide(s,m):
    if s==0 or m==0:
        return "Invalid"
    else:
        return s/m
    
