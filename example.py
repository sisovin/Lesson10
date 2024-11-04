# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# %%
""" 
import sys

value = "y"
count = 0

while value:
    count += 1
    print(count)
    value = input("Enter a value: ")
    if (count == 5):
        print("You have reached the maximum number of tries.")
        break
    else:
        print("You entered: " + value)
        print("Would you like to continue?")
        value = input("Enter 'y' to continue or 'n' to exit: ")               

sys.exit("Bye! Bye! Bye! 👋👋👋 \n\n")
"""
import sys

value = "y"
count = 0

while value.lower() == "y":
    count += 1
    print(count)
    if count == 5:
        print("You have reached the maximum number of tries.")
        break
    
    value = input("Enter a value: ")
    
    if value.lower() == "n":
        break
    
    if not value.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    
    if int(value) > 5:
        print("You entered a number greater than 5. Please try again.")
        continue
    
    print("You entered: " + value)
    print("Would you like to continue?")
    value = input("Enter 'y' to continue or 'n' to exit: ")

sys.exit("Bye! Bye! Bye! 👋👋👋 \n\n")

