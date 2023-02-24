# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane


# first we import what we need
import sys
import gzip

#create the list of variables so we can use it as a reference as we start coding
AA = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
hydrophobicity = [1,8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -1.6, -3.5, -4.5, -0.08, -0.07, 4.2, -0.09, -1.3]

# we need to take the file and then read the file
file = sys.argv[1]
def read(file):
	record = []
	sequence = ''
	with gzip.open(file, 'rt') as fp:
		for line in fp.readlines():
			line = line.rstrip()
			if len(line) == 0: continue 
			if line[0] == '>':
				if sequence != '':
					record.append(id)
					record.append(sequence)
				word = line.split()
				id = word[0][1:]
				sequence = ''
			else:
				sequence += line
		record.append(id)
		record.append(sequence)
	return record
# when I ran the lines above i did not get any errors so I know that it should be correct. 
# now that it reads the file it needs to calculate the KD for the AA and hydrophobicity

def KDcalculation(seq):
	sum = 0
	for i in range(len(seq)):
		for x in range(20):
			if dna[i] == AA[x]: sum += hydrophobicity[x]
		return sum/len(seq)
#When I ran this code with the one above, i got no errors either so im going to continue

#Need to see if proline is present in the sequence
def proline(seq):
	for a in seq:
		if a =='P': return False
	return True
	
#now I need to calculate the helix
def helix(seq, length, threshold):
	for i in range(len(seq) - length - 1):
		peptide = seq[i:i+length]
		if proline(peptide):continue # basically saying that if the petide chosen is proline then continue with the process. 
		if KDcalculation(peptide) > threshold: return True
	return False

# I ran this and got an error saying that proline was no defined.
# Need to see if proline is there or not in order to do the step above. 
#Found out that I was expecting it to give me a respinse when I didnt even write a print statement:/

for seq in read(file):
	if helix(file[0:30], 8, 2.5) and helix(file[30:], 11, 2.0):
		print(seq)
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
