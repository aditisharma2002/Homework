# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list


import sys
import gzip
 # start by defining the variables first
AA = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
comp_AA = [0] * len(AA)
total = 0

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlline():
		line = line.rstrip() # this is saying to strip the characters in newline
		if line.startswith('>'):
			continue 
			
		for i in range(len(AA)):
			a = AA[i]
			comp_AA[i] += line.count(a)

total = sum(comp_AA) # this gives us a list of the amino acids numbers with a probability amount.

for x in range(len(AA)):
	prob=comp_AA[x]/total
	print(AA[x], comp_AA[x], f'{prob:.3}')

# this does it by regit moving the white spaces and the C but doesnt give the full answer that we need
#with gzip.open(sys.argv[1], 'rt') as fp:
#	for line in fp.readlines():
#		line = line.rstrip()
#		if line.startswith('>'): continue
#		total += len(line)
#		for i in range(len(AA)):
#			A = AA[i]
#			comp_AA[i] += line.count(A)
			
#print(comp_AA)










#gives the name and id

#for line in fp.readlines():
#	id = word[0]
#	words = line.split()
#	print(id[1:], end='')
#	
#	words = line.split()
#	print(words[0][1:]) 

"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
