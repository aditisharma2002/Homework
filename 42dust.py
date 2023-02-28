# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import sys
import math
import mcb185

file = sys.argc[1]
window = int(sys.argv[2])
entropy_threshold = float(sys.argv[3])

#first step would be to make the entropy calculator 

def seq_entropy(seq):
	A = seq.count('A')/len(seq)
	T = seq.count('T')/len(seq)
	G = seq.count('G')/len(seq)
	C = seq.count('C')/len(seq)
	sequence = sequence.upper()
	sequence_list = list(sequence)
	vals = [A, T, G, C]
	h = 0
	assert(math.isclose(1.0, sum(vals)))
	for prob in vals:
		if prob != 0: h -= prob * math.log2(p)
	return h

#so we made just a regular entropy calculator but need to make one that does it for dna sequences

for name, sequence in mcb185.read_fasta(arg.s):
	sequence_list = list(seq.upper())
	for i in range(len(seq) - window +1):
		if seq_entropy(sequence[i:i+window]) < entropy_threshold:
			
			
print(seq_entropy(arg.s), arg.s)




"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
