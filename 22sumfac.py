# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

n = 5
x = 1
print (n, end=' ')


for i in range(x,n):
	x = x + (i+1)
	print (n, end=' ')
	
for i in range(x, n+1):
	x = x * 1
	print (n, end=' ')


"""
python3 22sumfac.py
5 15 120
"""
