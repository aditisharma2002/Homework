# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

# import the library 
import sys

nums= []
for value in sys.argv[1:]:
		nums.append(float(value))
nums.sort()

print(nums)


length = len(nums)
print("Count:", len(nums))
print("Maximum:", max(nums))
print("Minimum:", min(nums))


print("Mean:", sum(nums)/len(nums))

if length % 2 ==0:
	median = length//2
else:
print('Median:', length//2)


#mean = sum(nums)/len(nums)
#print("Mean:", f'{mean:.3f}')

sum = 0
for num in nums 
	sum += (val - mean) ** 2
variance = sum / len(nums)
std_dev = variance ** 0.5

print("Std_dev:", f'{std_dev:.3f}')


#if length % 2 == 0:
		#median = length//2
		#else: print("Median:", length//2)

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
