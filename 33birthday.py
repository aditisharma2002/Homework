# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list



import random
import sys

num_days = int(sys.argv[1])

num_people = int(sys.argv[2])

print(num_days, num_people)

trials = 1000
shared = 0

for trial in range(trails):
	calendar = [0] * num_days
	for i in range(num_people):
		birthday = random.randint(0, num_days - 1)
		if calendar[birthday] == 1:
			shared += 1
			break
		calendar[birthday] += 1
print(shared/trials)









# This is WRONG
#for trial in range(trials):
#	birthdays = []
#	for i in range(num_people):
#		birthday = random.randint(0, num_days - 1)
#		if birthday in birthdays:
#			shared += 1
#			break
#		birthday.append(birthday)
#print(shared/trial)

"""
python3 33birthday.py 365 23
0.571
"""

