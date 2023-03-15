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


import math
import mcb185
import argparse # this allows us to take inputs as arguments
import random # use it to test random values



#first we need to set up 
parser = argparse.ArgumentParser(description = 'Entropy Calculator')
parser.add_argument('file', type=str, metavar='<path>', help='need fasta file')#this is our argument that is always going to be true
parser.add_argument('-t', required=False, type=float, default= 1.4, metavar='<float>', help='need a value that is float [%(default).2f]')
parser.add_argument('-w', required=False, type=int, default= 11, metavar='<int>', help='need a value that is an interger [%(default).i]')
parser.add_argument('-s', required=False, action= 'store true' , , metavar='<float>', help='lowercase masking is OFF')
arg = parser.parse_args()

# calculating the entropy of the sequence
def entropyequation(window):
# we are going to first set up all the variables 
	nucleotides = ['A', 'T', 'G', 'C']
	H = 0 # where the entropy value will be put
	nucleotide_count = [0]*4 # this is the amount of each nucleotide that is found in the sequence. 
	nucleotide_probability = [] # this is the probability that that we find the nucleotides above in the sequence

	for nucleotide in window: 
		if nucleotide in nucleotides:
			nucleotide_counts[nucleotides.index(nucleotide)] += 1
	for count in nucleotide_counts:
		nucleotide_probability.append(count/len(window))
	for probability in nucleotide_probabilties: # this is the entropy equation that we use with the probabilities
		if probability != 0:
			H -= probability * math.log2(probabilty)
			
	return H 

# Now we are going to filter 
def entropy_filter(seq, window_len)
	window = seq[:window_len.upper()]
	fil_seq = seq.upper() # this copies the entire sequence and makes it uppercase
	
	for position in range(len(seq)):
		if position in range(len(seq) - window_len + 1): 
			if position != 0: # checking if it is in the range
				window = (window[1:]+ seq[pos + window_length - 1]).upper()
			H = entropyequation(window)
			
			if H < arg.t and arg.s == True:	
				fil_seq = fil_seq.replace(fil_seq[pos:pos + window_len], fil_seq[pos:pos + window_len].lower())
			elif H < arg.t and arg.s == False:
				fil_seq = fil_seq.replace(fil_seq[pos:pos + window_len], 'N'* window_len)
		if (pos + 1) % 60 == 0: # this is going to print the nucleotides in 60 per row
			yield(fil_seq[pos - 59: pos + 1])
	if len(seq) % 60 == 0: # this prints out the rest of the nucleotides in the sequence
		yield(fil_seq[len(seq) - (len(seq) % 60:)])

for row in mcb185.read_fasta(arg.file): # open and read the file
	print('>' + line[0]) # description
	for seq in line[1:]: # this is the filtered sequence that we want
		for row in entropy_filter(seq, arg.w):
			print(row)




				



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
