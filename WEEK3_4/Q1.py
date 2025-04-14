# Function to count uppercase and lowercase letters in a string.

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

s = input("Enter a string: ")
u, l = count_case(s)
print(f"Uppercase: {u}, Lowercase: {l}")
