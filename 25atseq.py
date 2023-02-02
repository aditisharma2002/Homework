# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

n = 30
dna = ''
count = 0

for i in range(n):
	r = random.randint(1,100)
	if r <= 30: 
		dna += 'A'
		count +=1
	elif r <= 60: 
		dna += 'T'
		count +=1
	elif r <= 80: 
		dna += 'C'
	else 		: 
		dna += 'G'

print(n,count/n, dna) 
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
