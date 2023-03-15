# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

import argparse
import mcb185

parser = argparse.ArgumentParser(description='Kmer counts in fasta file')
parser.add_argument('file, type=str, metavar='<path>', help='fasta file')
parser.add_argument('k', type=int, metavar='<int>', help='size of kmer')
arg = parser.parse_args()

kmers = {} #We are creating an empty dictionary called kmers so that we can store values in it later.

for line in mcb185.read_fasta(arg.file):
	for seq in line[1:]: # we want to make sure that we read only the sequence not the description
		for pos in range(len(seq)-arg.k+1): # we need the window to move over
			kmer = seq[pos:pos+arg.k]
			if kmer not in kmers: # counts the kmers
				kmers[kmer]= 1
			else:
				kmers[kmer] += 1
#prints results
for kmer in sorted(kmers):
	print(kmer,kmers[kmer])


"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
