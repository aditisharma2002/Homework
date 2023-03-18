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

# The first thing I will do is define my variables
file = sys.argv[1]
window = int(sys.argv[2])
entropythreshold = float(sys.argv[3])

def entropyequation(file, window, entropythreshold):
    for defline, sequence in mcb185.read_fasta(file): #this is saying read the FASA file and repetitively execute the same record in the file. 
        new_sequence = ''  # we create a new variable and assign it to a string that is empty. Allows us to add to the string as we go. 
        for position in range(len(sequence) - window + 1):
            next_sequence = sequence[position:position + window]
            A = 0 	# define the nucleotides
            T = 0
            G = 0
            C = 0
            for nucleotide in next_sequence: # Use the for loop to count the number of times that we get each nucleotide in the next_sequence sequence.
                if nucleotide == 'A': A += 1
                elif nucleotide == 'T': T += 1
                elif nucleotide == 'G': G += 1
                elif nucleotide == 'C': C += 1
            probability_A = A / window # now we have to assign variable:
            probability_T = T / window # basically calculating the probability that we will find the nucleotide A in the window length 
            probability_G = G / window
            probability_C = C / window
            probability_nucleotides = [probability_A, probability_T, probability_G, probability_C]
            H = 0 # we are giving the variable H the value 0 because this is what will store the entropy value later
            for probability_nucleotide in probability_nucleotides:
                if probability_nucleotide != 0: # here we are checking the probability_nucleotide and seeing if it is 0 or not
                    H += -(probability_nucleotide * math.log2(probability_nucleotide)) #entropy equation and the number is put in variable H
            if H < entropythreshold:
                new_sequence += 'N'
            else:
                new_sequence += next_sequence[0]
        yield defline, new_sequence

for defline, new_sequence in entropyequation(file, window, entropythreshold):
    print(defline)
    for position in range(0, len(new_sequence), 60):  # we make a loop that repetitively goes over the positions in the new_sequence and we are using a step of 60
        print(new_sequence[position: position + 60]) # prints the sequence in lines of 60 nucleotides each. 

#fixed the syntax errors and now the code runs







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
