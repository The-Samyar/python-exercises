# Calculates factorial of a non-negative number

n = int(input("Enter a number : "))

def factorial(n):
    if n == 1 or n == 0: 
        return 1
    
    return n * (factorial(n-1))

if n >= 0:
    print(f"Factorial of {n} is {factorial(n)}")
else:
    print("Number can not be negative")