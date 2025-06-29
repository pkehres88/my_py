# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math


def addNumbers():
    num1 = int(input("Input first number: "))
    num2 = int(input ("Input second number: "))
    sumNums = num1 + num2
    print("The sum is", sumNums)
    
def subtractNumbers():
    num1 = int(input("Input first number: "))
    num2 = int(input ("Input second number: "))
    diffNums = num1 - num2
    print("The difference is", diffNums)
        
def prodNumbers():
    num1 = int(input("Input first number: "))
    num2 = int(input ("Input second number: "))
    prodNums = num1 * num2
    print("The product is", prodNums)
    
def divNumbers():
    num1 = int(input("Input first number: "))
    num2 = int(input ("Input second number: "))
    divNums = num1 / num2
    print("The quotient (result) is", divNums)
    
def powerNum():
    num1 = int(input("Input number: "))
    num2 = int(input("Input power to raise number: "))
    powerNum = num1 ** num2
    print("Raising", num1, "to the", num2, "power is", powerNum)
    
def squareRootNum():
    num1 = float(input("Input number: "))
    result = math.sqrt(num1)
    print("The square root is", result)
    
opt = 99
while opt != 7:
    print("\nMenu") 
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Raise to a Power")
    print("6: Find the Square Root")
    print("7: End Program")
    
    opt = int(input("Input choice: "))
    
    if opt == 1:
        addNumbers()
    elif opt == 2:
        subtractNumbers()
    elif opt == 3:
        prodNumbers()
    elif opt == 4:
        divNumbers()
    elif opt == 5:
        powerNum()
    elif opt == 6:
        squareRootNum()
    

    
    
    
    
    
    
    