# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

#define our variables first so computer knows what each thing is
x = 1
n = 5
print(n, end='')

#running sum from 1...n
for i in range(x,n):
	x = x + (i+1)
print(x, end='')

x = 1
n = 5
for i in range(x, n+1):
	x = x * i
print(x, end='')
# now that I defined the variables for x and n again, it worked and I got 515120% but why is there no space in between them?


#running sum from 1...n
#for i in range(x,n):
	#x = x + (i+1)
#print(x, end='')
# when i only did this i got 515% so i need to add more

#for i in range(x, n+1):
	#x = x * i
#print(x, end='')
#when i ran only this I got 5120% so need to edit
#when I ran both the loops together I got 51515% so something went wrong





#running sum from 1..n
#for i in range(x,n): # we set variables above so computer knows what we mean
	#x = x + (i+1)
#for i in range(x, n+1):
	#x = x * i
#print(x, end='')

"""
python3 22sumfac.py
5 15 120
"""
