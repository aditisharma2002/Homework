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
