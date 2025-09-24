## vars
#imort numpy as np


nums = [float(input(f"Enter number {i+1}: ")) for i in range(10)]


avg = sum(nums) / len(nums)
var = sum((x - avg) ** 2 for x in nums) / len(nums)

print("Average:", avg)
print("Variance:", var)
print("Maximum:", max(nums))
print("Minimum:", min(nums))
