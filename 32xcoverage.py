# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

# import what we need
import random
import sys

#need to make a list without using title in command line 
list = sys.argv[1:]

# length of list is 3 and there are variables that we need for it to follow
genome_size = int(list[0])
read_number = int(list[1])
read_length = int(list[2])

genome = []
genome = [0] * genome_size

# we need the read number to correspond to the positions on the genome 

for position in range(read_number):
	begin = random.randint(0, genome_size - read_length)

#when there is an overlap in the genome, we want there to be a +1 
# make another for loop in order to do this
	for overlap in range(begin, begin + read_length):
		genome[overlap] += 1

# i ran the program until now and I have not gotten any errors so I know that there are no mistakes yet because it would have told me what line the error would have been in.

# now we need to do the min, max and sum 
# cannot use min, max because they are functions
minimum = genome[read_length - 1]
maximum = genome[read_length - 1]
sum = 0

# we need the program to go through the genome at the different read postions that are present.
for count in genome[read_length - 1: -read_length]:
	if minimum > count:
		minimum = count 
	if maximum < count:
		maximum = count
	sum += count

# I thought this was the end but realized when I ran it the correct thing did not show up.

# find the average but we need to make sure not to include the ends. 
average = sum / (genome_size - 2 * read_length)

print(minimum, maximum, f'{average:.5f}')



"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
