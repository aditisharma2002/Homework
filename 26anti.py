# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax


dna = 'ACTGAAAAAAAAAAA'
dna = 'ACTGAAAAAAAAAAA'
for nt in dna[::-1]: # this is saying that we start at the beginning of the sequence, end at the end , and go in steps of 1 in reverse
	if nt == 'A' :
		print('T')
	elif nt == 'T':
		print('A')
	elif nt == 'G':
		print('C')
	elif nt == 'C':
		print('G')
	else:
		print('C')	

#when i changed the dna[::1 to dna(::-1)] it showed the DNA in reverse


#for nt in dna[::1]: # this is saying that we start at the beginning of the sequence, end at the end , and go in steps of 1 in reverse
#	if nt == 'A' :
#		print('T')
#	elif nt == 'T':
#		print('A')
#	elif nt == 'G':
#		print('C')
#	elif nt == 'C':
#		print('G')
#	else:
#		print('C')	
		
#this gave me the sequence but like the opposite of it which is not what we want. 




"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
