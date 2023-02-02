# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

def running_sum_factorial(n):
    running_sum = 0
    factorial = 1
    for i in range(1, n + 1):
        running_sum += i
        factorial *= i
    return running_sum, factorial

n = 5
running_sum, factorial = running_sum_factorial(n)
print("Running sum from 1 to", n, ":", running_sum)
print("Factorial of", n, ":", factorial)


"""
python3 22sumfac.py
5 15 120
"""
