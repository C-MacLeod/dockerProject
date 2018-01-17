#!/usr/bin/python

import sys

def isPrime(args):
        numToCheck = int(args[0])
        lower = int(args[1])
        upper = int(args[2])

        if (numToCheck % 2 == 0):
           return False
             
        for x in range(lower, upper):
           #print x
           if (numToCheck % x == 0):
              return False

        return True

def main():
    # print command line arguments
    args = []
    for arg in sys.argv[1:]:
#        print arg
         args.append(arg)
    print (isPrime(args))

if __name__ == "__main__":
    main()


