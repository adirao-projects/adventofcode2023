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
		input_vals.append([x for x in line.strip().split(' ')])

	return input_vals


def part1(input_vals):
	sum_calib_val = 0
	for line in input_vals:
		strip_line = [int(x) for x in list(line[0]) if x.isdigit()]
		sum_calib_val += int(str(strip_line[0])+str(strip_line[-1]))
		

	return sum_calib_val


def part2(input_vals):
	def first_digit_crawler(line):
		word=''
		for char in line:
			if char.isdigit():
				return str(char)
			else:
				word+=char
				for num in numbers:
					if num in word:
						return str(numbers[num])

	def last_digit_crawler(line):
		word=''
		for char in line[::-1]:
			if char.isdigit():
				return str(char)
			else:
				word=char+word
				for num in numbers:
					if num in word:
						return str(numbers[num])

	numbers = {'one' : 1, 'two' : 2, 
			'three' : 3, 'four' : 4, 
			'five' : 5, 'six' : 6,
			'seven' : 7, 'eight' : 8,
			'nine' : 9, 'zero' : 0} 

	sum_calib_val = 0
	for line in input_vals:
		new_line = line[0]
		first = first_digit_crawler(new_line)
		last = last_digit_crawler(new_line)

		sum_calib_val += int(first + last)

	return sum_calib_val

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
 
	