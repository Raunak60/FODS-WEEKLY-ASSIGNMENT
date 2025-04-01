# Count occurrences of 'a' in a list of names.

names = input("Enter names separated by space: ").split()
a_count = sum(name.lower().count('a') for name in names)
print("Total occurrences of 'a':", a_count)