import math


Num = int(input("Enter a number to find its factorial: "))


def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers."
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


Answer = factorial(Num)
print(f"The factorial of {Num} is: {Answer}")




num1 = float(input("Enter a number for math calculations: "))

print(f"Square root: {math.sqrt(num1)}")
print(f"Natural Logarithm: {math.log(num1)}")
print(f"Sine (radians): {math.sin(num1)}")