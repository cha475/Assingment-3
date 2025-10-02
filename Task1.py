
number = int(input("Enter a number: "))

def factorial(number):
    if number <2 :
        return 1
    else:
        return number * (factorial(number - 1))
    

result = factorial(number)

print(f"Factorial of {number} is : {result}")

