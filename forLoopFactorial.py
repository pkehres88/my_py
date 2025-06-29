# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Factorial Program")
stopnum  = int(input("Input factorial number: "))
theProduct = 1
index = 1
while index <= stopnum:
    theProduct = theProduct * index
    index = index + 1
print("Factorial is:", theProduct)