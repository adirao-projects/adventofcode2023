import argparse
import sys

sys.path.append('../')

#import Algorithms
#from ComplexDataStructures import Queue

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Part", type=int, help = "Which Part", default=0)
parser.add_argument("-t", "--Test", action="store_true", help = "Uses test inputs")
args = parser.parse_args()

import numpy as np
from itertools import combinations 

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        
    def enqueue(self, value):
        i=self.size-1
        while self.queue[i]==None:
            if i<0:
                return False
            else:
                i=i-1
        self.queue[i] = value
        
        return True
    
    def dequeue(self):
        i=self.size-1
        value = self.queue[-1]
        while self.queue[i]!=None:
            if i!=0:
                self.queue[i] = self.queue[i-1]
            else:
                self.queue[i]=None
                
        return value

def openFile(test_mode=False):
    """
    Parameters
    ----------
    test_mode : Boolean
        Specifies whether to use the test 
        inputs or the full input.

    Returns
    -------
    input_vals : list
        Contains all inputs in a list format.

    """
    if test_mode:
        f = open('test_inputs.txt','r').readlines()
    else:
        f = open('inputs.txt','r').readlines()
    
    return f

def inputProcess(f):
    """
    Parameters
    ----------
    f : file
        The file that is to be processed input input values

    Returns
    -------
    input_vals : list
        Processed input values.

    """
    input_vals = []
    for line in f:
        return line.strip()

    return input_vals


def part1(input_vals):
	buff = []

	for i, char in enumerate(input_vals):
		buff.append(char)
		if len(buff)>4:
			_ = buff.pop(0)

		if len(set(buff))==4:
			return i+1

def part2(input_vals):
	buff = []

	for i, char in enumerate(input_vals):
		buff.append(char)
		if len(buff)>14:
			_ = buff.pop(0)

		if len(set(buff))==14:
			return i+1

def optimized(input_vals):
	raise NotImplementedError

if __name__=="__main__": 
    f = openFile(args.Test)  

    input_vals = inputProcess(f)
    
    if args.Part == 1:
        output = part1(input_vals)

    elif args.Part == 2:
        output = part2(input_vals)
    
    elif args.Part == 0:
  	     output = optimized(input_vals)
    
    print(output)
 
    