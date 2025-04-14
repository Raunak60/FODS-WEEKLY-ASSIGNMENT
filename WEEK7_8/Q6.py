# Input array of numbers, sort and slice.

import numpy as np
numbers = list(map(int, input("Enter at least 10 numbers separated by spaces: ").split()))
numbers.sort()
print("Sorted Array:", numbers)
print("Slicing 2-5:", numbers[2:6])
print("Slicing 5-8:", numbers[5:9])
print("Slicing 2-9:", numbers[2:10])
