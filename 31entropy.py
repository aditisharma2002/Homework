# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


import math 
import sys 

# need to make a list first
list = sys.argv[1:]
tot = 0

for i in range(len(list)):
	try: 
		list[i] = float(list[i])
		tot += list[i]
	except:
		print("Please enter your number")


if i > 1.0:
	print("ERROR. Does not sum to 1.0")
else:	
	H = 0
	for i in range(len(list)):
		H = H + -(list[i] * math.log(list[i],2))
	print(f'{H:.4}')










#list = []
#i = 0
#i = sys.argv([1:])
#H = -sum(pi * log(pi))
# it says that I have the wrong syntax in line 19:?/




"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
