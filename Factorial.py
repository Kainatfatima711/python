def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n - 1)
    
number = int(input("Enter the number for which you want to find Factorial: "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    print(f"The Factorial of {number} is {factorial(4)} ")
