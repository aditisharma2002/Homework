# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for a in range(0, len(dna), 3): # here we are saying for the variable in the range of 0 to the length of the dna using step of 3.
	codon = dna[a: a + 3]
	print(codon)  

"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
