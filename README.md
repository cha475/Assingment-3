# Assingment-3


TASK1.py
------

code used
--------

number = int(input("Enter a number: "))

def factorial(number):
    if number <2 :
        return 1
    else:
        return number * (factorial(number - 1))
    

result = factorial(number)

print(f"Factorial of {number} is : {result}")



Execution
--------
python Task1.py


Output
-----

Enter a number: 5
Factorial of 5 is : 120





Task2.py
------

Code Used
------
import math 

number = int(input("Enter a number: "))


print(f"The square root of {number} is {(math.sqrt(number))}")
print(f"The logarithm of {number} is {(math.log(number))}")
print(f"The sine of {number} is {(math.sin(number))}")



Execution
--------

python Task2.py

Output
-----

Enter a number: 25
The square root of 25 is 5.0
The logarithm of 25 is 3.2188758248682006
The sine of 25 is -0.13235175009777303
