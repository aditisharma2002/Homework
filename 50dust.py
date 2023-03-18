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
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='Entropy Calculator')
parser.add_argument('file', type=str, metavar='<path>', help='fasta file')
parser.add_argument('-t', required=False, type=float, default=1.4, metavar='<float>', help='float [%(default).2f]')
parser.add_argument('-w', required=False, type=int, default=11, metavar='<int>', help='integer [%(default)i]')
parser.add_argument('-s', required=False, action='store_true', help='lowercase masking is OFF')
args = parser.parse_args()

def entropy(probs):
	assert(math.isclose(1.0, sum(probs))) #check sum of the probabilities
	h = 0
	for p in probs:
		if p != 0: h -= p * math.log2(p)
	return h # here we get out entropy
	
def seq_entropy(seq):
	A = seq.count('A')/len(seq)
	C = seq.count('C')/len(seq)
	G = seq.count('G')/len(seq)
	T = seq.count('T')/len(seq)
	return entropy([A, C, G, T])

for name, seq in mcb185.read_fasta(sys.argv[1]):
	seq = seq.upper() # convert the sequence to uppercase
	seq1 = list(seq)
	for i in range(len(seq) - arg.w + 1):
		win = seq[i: i + arg.w]
		if seq_entropy(win) < arg.t:
			for j in range(i, i + arg.w):
				if arg.lowercase: seq1[j] = seq[j].lower()
				else: seq1[j] = 'N'
	seq = ''.join(seq1)
	print(f'>{name}')
	for i in range(0, len(seq), 60):
		print(seq[i: i + 60]) # printed in 60 characters each time
		
		
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