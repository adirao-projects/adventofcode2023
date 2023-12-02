import argparse
import sys

sys.path.append('../')

#import Algorithms
#import ComplexDataStructures

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Part", type=int, help = "Which Part", default=0)
parser.add_argument("-t", "--Test", action="store_true", help = "Uses test inputs")
args = parser.parse_args()

import numpy as np
from itertools import combinations 

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

def testOutput(answer: int, test_value:int) -> bool:
	"""
	Parameters
	----------
	answer : int
		The answer to be checked.

	Returns
	-------
	bool
		True if the answer is correct, False otherwise.

	"""
	if answer == test_value:
		print(f'{answer} is correct!')
		return True
	else:
		print(f'{test_value} expected, {answer} received.')
		return False

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
		line = line.strip()
		input_vals.append([x for x in line.split(' ')])

	return input_vals

def part1(inputs):
	raise NotImplementedError

def part2(inputs):
	raise NotImplementedError    

def optimized(inputs):
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
	
	TEST_VALUE = 0
	testOutput(output, TEST_VALUE)

	print(output)
 
	