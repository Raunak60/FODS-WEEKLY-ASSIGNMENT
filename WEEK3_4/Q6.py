# Store integers between 1-100 in a list

def filter_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 'stop' to finish): ")
        if num.lower() == 'stop':
            break
        if num.isdigit() and 1 <= int(num) <= 100:
            numbers.append(int(num))
    return numbers

print("Filtered Numbers:", filter_numbers())