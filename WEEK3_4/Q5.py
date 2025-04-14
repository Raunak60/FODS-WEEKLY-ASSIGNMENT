# Calculator with basic arithmetic functions.

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else 'Error: Division by zero'
def trunc_div(a, b): return a // b if b != 0 else 'Error: Division by zero'
def modulus(a, b): return a % b
def exponent(a, b): return a ** b
a, b = 10, 3

print("Add:", add(a, b))           
print("Subtract:", subtract(a, b)) 
print("Multiply:", multiply(a, b)) 
print("Divide:", divide(a, b))     
print("Trunc Div:", trunc_div(a, b)) 
print("Modulus:", modulus(a, b))   
print("Exponent:", exponent(a, b)) 

