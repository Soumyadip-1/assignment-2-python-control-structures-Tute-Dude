# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

num = int(input("Enter a number to check even/odd : "))
if num%2==0:
    print("The number",num, "is even")
else:
    print("The number",num, "is odd")

# output:
#    Enter a number to check even/odd : 20
#    The number 20 is even
