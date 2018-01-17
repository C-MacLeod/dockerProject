#!/usr/bin/python

import sys
from primeUtil import isPrime

# big prime for testing: 982451653 
# big non prime for testing 982451657
# 50 digit prime 22953686867719691230002707821868552601124472329079
# 10 digit 3367900313



def main():
	args = []
	list = [] # list of tuples to process
	# just grab the prime from the command line and put into var
	for arg in sys.argv[1:]:
		#print arg
		args.append(arg)
		target = int(arg)
	# now we have loaded the target prime into the list
	#
	# at some point we'll want to divide up the search and put those numbers
	# each into their own list to be processed by the minion workers

	# this code should not know the number of workers
	# but would should pick some number to start with ... then
	# parse the list into "those" chuncks
	# 
	# let's make the chunks 100 long

	if (int(args[0]) > 100):
		# proceed to parse into 100 chuncks
		# output to log ... TODO
		print ("more then 100 to do!")
		# this code creates the first fixed tuple
		listLocal = []
		listLocal.append(target)
		listLocal.append(3)
		listLocal.append(int(target/2))
		# want these put into a queue as they are created
		list.append(listLocal)
		
		# this code processes the next set of tuples 
		# up to the possible final tuple handled below
		finalValueOfI = 0
		for i in range(100,int(target/2), 100):
			listLocal = []
			listLocal.append(target)
			listLocal.append(i+1)
			listLocal.append(i+100)
			# want these put into a queue as they are created
			list.append(listLocal)
			finalValueOfI = i
		# block to pick up final piece of processing not
		# performed by the loop above, may not be needed
		#
		if (finalValueOfI != 0 and finalValueOfI <= target/2):
			listLocal = []
			listLocal.append(target)
			listLocal.append(finalValueOfI)
			listLocal.append(int(target/2))
			# want these put into a queue as they are created
			list.append(listLocal)
			
		
	else:
		# we have less then 100 ... just create 1 chunk
		listLocal = []
		listLocal.append(target)
		listLocal.append(3)
		listLocal.append(int(target/2))
		# send into queue 
		list.append(listLocal)

	for listToProcess in list:
		print (listToProcess)
	#print (isPrime(args))

if __name__ == "__main__":
	main()


