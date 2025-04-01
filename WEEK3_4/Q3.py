 
# Function to check if a number is an Armstrong number.

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

n = int(input("Enter a number: "))
print("Armstrong Number" if is_armstrong(n) else "Not an Armstrong Number")