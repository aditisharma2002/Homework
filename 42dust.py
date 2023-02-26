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
def entropy(probability):
	assert(math.isclose(1.0, sum(probability)))
	h = 0
	for prob in probability:
		if prob != 0: h -= prob * math.log2(p)
	return h

#so we made just a regular entropy calculator but need to make one that does it for dna sequences
def seq_entropy(seq):
	A = seq.count('A')/len(seq)
	T = seq.count('T')/len(seq)
	G = seq.count('G')/len(seq)
	C = seq.count('C')/len(seq)
	return entropy([A, T, G, C])
	
for thing, seq in MCB185.read.fasta(sys.argv[1]):
	seqX = list(seq)
	for i in range(len(seq) - window + 1):
		w = seq[i: i + w]
		e = seq_entropy(w)	
	seq =''.join(seqX)
	print(seq)





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
