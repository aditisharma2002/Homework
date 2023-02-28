# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import sys
import math
import mcb185
import argparse #using parse makes the code more executable
import random

file = sys.argv[1]
window = int(arg.w)
entropy_threshold = float(arg.t)

#first we need to set up 
parser = argparse.ArgumentParser(description = 'Entropy Calculator')
parser.add_argument('file', type=str, metavar='<path>', help='need fasta file')#this is our argument that is always going to be true
parser.add_argument('-t', required=False, type=float, default= 1.4, metavar='<float>', help='need a value that is float [%(default).2f]')
parser.add_argument('-w', required=False, type=int, default= 11, metavar='<int>', help='need a value that is an interger [%(default).i]')
parser.add_argument('-s', required=False, action= 'store true' , , metavar='<float>', help='lowercase masking is OFF')
arg = parser.parse_args()

print(arg.s)
print(arg.t, arg.w, arg.s)


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
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
