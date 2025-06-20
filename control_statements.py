#allows execution based on conditions (if, asif, else)

num = -2

if num > 0:
    print("This number is positive")
elif num == 0: #this is elseif, it's used when there's more than two conditions, it also has a specified conndition, only 'else' doesn't have a condition
    print("This number is zero")  
else: 
    print("Number is negative") 
    
#example input values with control statements
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
        print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    