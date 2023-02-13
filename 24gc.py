# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

#first we are going to assign values to the variables so that we can store other values in them later on
g = 0
c = 0

#now we have to make it so that every time there is a G or C, 1 is added.
for BP in dna:
	if BP == 'G':
		g = g + 1
	elif BP == 'C':
		c = c + 1
	gc_count = c + g
# we want it to be like an average and that is why we take the value that we get above and then divide by the total in the dna.
print(f'{gc_count/len(dna):.2f}')
#now I got 0.42 as the answer


#first we are going to assign values to the variables so that we can store other values in them later on
#g = 0
#c = 0

#now we have to make it so that every time there is a G or C, 1 is added.
#for BP in dna:
#	if BP == 'G':
#		g = g + 1
#	elif BP == 'C':
#		c = c + 1
#print(BP)
# did the same thing and only printed T 


# first we are going to assign values to the variables so that we can store other values in them later on
#G = 0
#C = 0

#now we have to make it so that every time there is a G or C, 1 is added.
#for BP in dna:
	#if BP == 'G':
	#	G = G + 1
	#elif BP == 'C':
	#	C = C + 1
#print(BP)
# when I did this, I got T which is definitely not what we want.
# maybe the computer is getting confused because I am using G and C as variable but they are also in the sequence. 
# changed G and C to g and c
"""
python3 24gc.py
0.42
"""
