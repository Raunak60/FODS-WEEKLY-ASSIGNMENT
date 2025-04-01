# Create random integer array, sort, and reshape.

import numpy as np
rand_integers = np.random.randint(1, 100, 10)
print("Original Array:", rand_integers)
rand_integers.sort()
print("Sorted Array:", rand_integers)
reshaped_array = rand_integers.reshape(2, 5)
print("Reshaped Array:\n", reshaped_array)