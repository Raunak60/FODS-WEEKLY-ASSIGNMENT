# Generate a random array of shape (a, b) and print the array and average.

import numpy as np
a = int(input("Enter number of rows: "))
b = int(input("Enter number of columns: "))
rand_array = np.random.rand(a, b)
print("Random Array:\n", rand_array)
print("Average:", np.mean(rand_array))