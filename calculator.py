def calculator():
   x = float(input('Enter a number to perform an operation: '))
   y = float(input('Enter a number to perform an operation: '))
   print("The operations currently available are addition(+), subtraction(-), division(/) and multiplication(*)")
   operator = input("Enter the 1 operator to perform your operation: ")

   if operator == '+':
     print(f"The sum between {x} and {y} is {x+y}")
   elif operator == '-':
     print(f"The subtraction between {x} and {y} is {x-y}")
   elif operator == '/':
     print(f"The division of {x} and {y} is {x/y}")
   elif operator == '*':
     print(f"The multiplication of {x} and {y} is {x*y}")
   else:
     print("Try typing one of the operators indicated for the operation, +, -, / or * :")

calculator()
