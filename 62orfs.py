# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome


import argparse
import mcb185
import re

parser = argparse.ArgumentParser(description='Find ORFs in the genome given in the FASTA file and be able to give results regarding the parent sequence identifier, range, and the first 10 amino acids of the protein.')
parser.add_argument('file', type=str, metavar='<path>', help='Fasta file')
parser.add_argument('-l', type=int, metavar='<int>', required=False, default=300, help='the minimum ORF size [%(default)i]')
arg = parser.parse_args()

def get_orfs(iden, strand, seq):
    anti = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    if strand == '-':
        aseq = ''
        for nucleotide in seq[::-1]:
            aseq += anti[nucleotide]
        seq = aseq

    for i in range(len(seq)-2):
        if i >= len(seq)-arg.l*3:
            break
        codon = seq[i:i+3]

        if codon == 'ATG':
            pseq = mcb185.translate(seq[i:])
            if pseq is None:
                continue
            pseq = pseq.split('*')[0]
            start = i+1

            if len(pseq) < arg.l/3:
                continue
            elif strand == '+':
                yield(iden, start, start+len(pseq)*3-1, '+', pseq[:10])
            elif strand == '-':
                yield(iden, len(seq)-start-len(pseq)*3+2, len(seq)-start+1, '-', pseq[:10])

print('Parent\tBegin\tEnd\tStrand\tProtein')
for desc, seq in mcb185.read_fasta(arg.file):
    iden = re.search('\S+', desc)
    iden = iden.group()
    for orf in get_orfs(iden, '+', seq):
        print('\t'.join(map(str, orf)))
    for orf in get_orfs(iden, '-', seq):
        print('\t'.join(map(str, orf)))











""""






import argparse 
import mcb185
import re # this will help us look for the sequence identifier

parser = argparse.ArgumentParser(description='Find ORFs in the genome given in the FASTA file and be able to give results regarding the parent sequence identifier, range, and the first 10 amino acids of the protein.')
parser.add_argument('file', type=str, metavar='<path>', help='Fasta file')
parser.add_argument('-l', type=int, metavar='<int>', required=False, default=300, help='the minimum ORF size [%(default)i]')
arg = parser.parse_args()

# First we need to find all the possible ORFs
def get_orfs(iden, strand, seq):
	anti = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}# these are the variables that we will be using
	if strand == '-': # this is the statement that will give us the anti-sense strand
		aseq = '' # creating empty variable so that the empty variable that we get can go here
		for nucleotide in seq[::-1]: aseq += anti[nucleotide]
		seq = aseq
	
	for i in range(len(seq)-3): #check for start codon and returning codons
		if i >= len(seq)-arg.l: # this helps us make sure that the frame matches the minimum number of codons
			break
		codon = seq[i:i+3] # this is the sliding window
		
		if codon == 'ATG': # we need to get the protein sequence using a generic START codon. 
			pseq = mcb185.translate(seq[i:]) #if the start codon is ATG, the program will use the mcb185 to translate the sequence and then the value will be stored in the variable pseq
			if pseq is None: # if the sequence cannot be translated, the computer moves on
				continue
			pseq = pseq.split('*')[0]
			start = i+len(pseq)*3+3 # this is the start of the ORF
			
			if len(pseq) < arg.l/3: # this is checking the minimum length
				continue
			elif strand == '+': # use this to report the ORF data based on the sequence that we have given the code to analyze
				yield(iden, i+1, start, '+', pseq[:10]) #forward direction
				continue
			elif strand == '-': #reverse direction
				yield(iden, len(seq)-start+1, len(seq)-i, '-', pseq[:10])
				continue
				
for desc, seq in mcb185.read_fasta(arg.file):
	iden = re.search('\w+.\S', desc)
	iden = iden.group()
	# to print the results
	for iden, start, end, strand, pseq in get_orfs(iden, '+', seq):
		print(iden, start, end, strand, pseq)
	for iden, start, end, strand, pseq in get_orfs(iden, '-', seq):
		print(iden, start, end, strand, pseq)


python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
