#  Dictionary operations.

dic1, dic2, dic3 = {1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}
nums = {**dic1, **dic2, **dic3}
nums[7] = 70
nums[3] = 80
del nums[3]
sum_values = sum(nums.values())
mul_values = 1
for v in nums.values(): mul_values *= v
max_val, min_val = max(nums.values()), min(nums.values())
print("Final Dictionary:", nums)
print("Sum:", sum_values, "Product:", mul_values, "Max:", max_val, "Min:", min_val)