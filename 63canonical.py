# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import mcb185
import re
import sys
import gzip

filename = sys.argv[1]
seq = '' # creating an empty variable so that the sequence can go in here later.
# the code below is used to extract the DNA sequence and put it into the variable seq
with gzip.open(filename, 'rt') as fp: # the file is opened and read in a text format
	for line in fp: 3 use this for loop to find the ORIGIN 
		if line.startswith('ORIGIN'):
			break
	for line in fp.readlines(): read the line and the split it to make a word list and join back together
		f = line.split()
		seq += ''.join(f[1:]) # this is the sequence that is going into the seq variable
seq = seq.upper() # we want the value in the seq variable to be Uppercase

# the code below is used to find the coordinates
start_coors = {} # assigning an empty variable so that we can 
with gzip.open(filename, 'rt') as fp: # this opens the gzip file and reads
	for line in fp.readlines():
		if line.startswith('CDS'): # checking to see if the line starts with CDS
			coordinates = re.search('(\d+)\.\.(\d+)', line)
			beginning = int(coordinates.group(1)) # extracts beginning
			end = int(coordinates.group(2)) # extracts end
			if 'complement' in line:
				startcoor = mcb185.anti(seq[end - 3: end]) # if the line containt the complement, then program will analyze the reverse seqeuence
			else: # if not then we get the sequence from the seq 
				startcoor = seq[beginning - 1: beginning + 2]
			if startcoor not in startcoors: 
				startcoors[startcoor] = 0
			startcoors[startcoor] += 1
# prints results			
for startcoor in startcoors:
	print(startcoor, startcoors[startcoor])




"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
