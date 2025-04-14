# Perimeter of a rectangle with length 9 and width 6
length = 9
width = 6
perimeter = 2 * (length + width)
print("Perimeter of rectangle:", perimeter)

# 2 to the 10th power
print("2^10:", 2 ** 10)

# 7 factorial minus 5 factorial
import math
result = math.factorial(7) - math.factorial(5)
print("7! - 5!:", result)

# Your forename multiplied by 5
name = input("Enter your forename: ")
print(name * 5)

# Your name left justified 15 spaces
name = input("Enter your name: ")
print(name.ljust(15, ' '))

# PI to 5 decimal places
print("PI to 5 decimal places:", format(math.pi, ".5f"))

# 200 modulus 12
print("200 % 12:", 200 % 12)

# 7.2 as an integer value
print("Integer value of 7.2:", int(7.2))


# 9. The Unicode encoding for your name
name = input("Enter your name: ")
unicode_values = [ord(char) for char in name]
print("Unicode values:", unicode_values)