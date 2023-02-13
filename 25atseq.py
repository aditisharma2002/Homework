# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random #in question it says that we need to import a random sequence
seq_len = 30
seq = ''
fraction_AT = 0.6
at = 0
# here we are saying that if the basepair in the sequence of nucleotides is A or T, then add 1
# then we say in the en
for NT in range(seq_len):
	for BP in seq:
		if BP =='A' or BP == 'T':
			at = at + 1
	r = random.random() # use this because we want random float numbers 
	if r <= fraction_AT: seq = seq + random.choice('AT')
	else:
		seq = seq + random.choice('CG')
print(len(seq), at/len(seq), seq)
# when i did this, I got the wrong values for the decimal and the sequence after it but I think this is because a random sequence is picked every time.
"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
