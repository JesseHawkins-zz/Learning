#!/usr/bin/env python

'''
SOURCE: http://www.programming-challenges.com/pg.php?page=downloadproblem&probid=110101&format=html

Consider the following algorithm to generate a sequence of numbers. Start with an integer n. If n is even, divide by 2. If n is odd,
multiply by 3 and add 1. Repeat this process with the new value of n, terminating when n = 1. For example, the following sequence
of numbers will be generated for n = 22:

22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

It is conjectured (but not yet proven) that this algorithm will terminate at n = 1 for every integer n. Still, the conjecture holds
for all integers up to at least 1,000,000.

For an input n, the cycle-length of n is the number of numbers generated up to and including the 1. In the example above, the cycle
length of 22 is 16. Given any two numbers i and j, you are to determine the maximum cycle length over all numbers between i and j,
including both endpoints.

Input

The input will consist of a series of pairs of integers i and j, one pair of integers per line. All integers will be less than
1,000,000 and greater than 0.

Output

For each pair of input integers i and j, output i, j in the same order in which they appeared in the input and then the maximum
cycle length for integers between and including i and j. These three numbers should be separated by one space, with all three
numbers on one line and with one line of output for each line of input.

Sample Input

1 10
100 200
201 210
900 1000

Sample Output

1 10 20
100 200 125
201 210 89
900 1000 174
'''

import sys # needed for sys.stdout.write()

# take arguments from command line
i = sys.argv[1]
j = sys.argv[2]
z = sys.argv[3] # I need to figure out how to not crash when this isn't used.

# No idea why these have to be declared here. I am learning about global variables and think that setting them as global in the
# function should be specific. I guess that value declared in the function must exist before being assigned from within the function.
maxCycles = 0
cycledNumberToGetMaxCycles = 0

# function to do the cycling
def cycle(n, showWork = 0): # showWork set to False by default
	# global setting here allows the function to update these variables outside the function
	global maxCycles
	global cycledNumberToGetMaxCycles
	if showWork == 1: # this happens many times: make it fancy or keep it plain
		div = "-" * 80 # creates a line of dashes 80 characters
		sys.stdout.write(div) # prints the line of dashes
		print "running cycles on: ", str(n) # tells user which number is currently being cycled
		sys.stdout.write(str(n) + " ") # starts the line of cycle results with the currently cycling number
	numOfCyclesRan = 0 # counter for how many cycles were ran for the currently cycling number
	numBeingCycled = n # the currently cycling number
	numOfCyclesRan += 1 # add one to count this first cycle
	while n != 1: # continue until the cycling number is reduced to 1
		if n % 2 == 0: # test cycling number to see if it's divisible by 2 (aka if it's even)
			if showWork == 1: # this happens many times: make it fancy or keep it plain
				sys.stdout.write(str(n / 2) + " ") # divide the cycling number in half and append it to the line of answers
			n = n / 2 # set value of cycling number to half's it's current value 
		elif n == 1: # test cycling number to see if it's 1
			if showWork == 1: # this happens many times: make it fancy or keep it plain
				sys.stdout.write(n, " ") # append cycling number, now 1, to the line of answers
		elif n % 2 != 0: # test cycling number to see if it's not divisible by 2 (aka if it's odd) - note that test for 1 came before this step
			if showWork == 1: # this happens many times: make it fancy or keep it plain
				sys.stdout.write(str(n * 3 + 1) + " ") # multiply the cycling number by 3, add 1, and append it to the line of answers
			n = n * 3 + 1 # set value of cycling number to it's current value multiplied by 3, then add 1
		numOfCyclesRan += 1 # increment the number of cycles ran
	if showWork == 1: # this happens many times: make it fancy or keep it plain
		print "" # print empty line to end the line of answers
		print "number of cycles ran: ", str(numOfCyclesRan) # show how many cycles where ran to get the currently cycling number down to 1 
		sys.stdout.write(div) # prints the line of dashes
	if numOfCyclesRan > maxCycles: # test is number of cycles ran for currently cycling number is highest from all of those ran before it
		maxCycles = numOfCyclesRan # set maxCycles to number of cycles ran for currently cycling number
		cycledNumberToGetMaxCycles = numBeingCycled # set cycledNumberToGetMaxCycles to the number used at the start of the current cycle

	## debug
	# print "   maxCycles: ", str(maxCycles)
	# print "   numOfCyclesRan: ", str(numOfCyclesRan)
	# print "   cycledNumberToGetMaxCycles: ", str(cycledNumberToGetMaxCycles)

for foo in range(int(i), int(j) + 1): # for every value between the first arg (i) and the second arg (j)
	cycle(foo, int(z)) # run the cycle function on foo and pass the third arg (z) to the function

print str(i), str(j), str(maxCycles) # print answer in format: i j <maxCycles>

## debug
# print "highest number of cycles ran: ", str(maxCycles)
# print "cycled number at that time: ", str(cycledNumberToGetMaxCycles)

## pauses screen when used as an executable script
# raw_input("press enter to exit")