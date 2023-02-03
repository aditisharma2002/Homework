# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

def reverse(dna):
	sequence = " "
	for nt in dna: 
		if nt == 'A' :
			sequence = 'T' + sequence
		elif nt == 'T':
			sequence = 'A' + sequence
		elif nt == 'G':
			sequence = 'C' + sequence
		elif nt == 'C':
			sequence = 'G' + sequence
	return sequence	


dna = 'ACTGAAAAAAAAAAA'


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
