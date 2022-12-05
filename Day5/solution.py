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

import re


class Stack:
	def __init__(self, size: int) -> None:
		self.size = size
		self.stack = [None]*size
		self.height = 0
		
	def push(self, value):
		i=0
		while self.stack[i]==None:
			if i == self.size-1:
				return False
			else:
				i+=1 

		self.stack[i] = value
		self.height += 1
		return True
		
	def pop(self):
		i = self.size-1
		while self.stack[i]==None:
			if i == 0:
				return False
			else:
				i=i-1
		value = self.stack[i]
		self.stack[i]=None
		
		return value

	def get_height(self):
		return self.height


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
	input_vals = [] # list of stacks
	sequence = []
	stacks = []
	containers = True
	lst = []
	for line in f:

		if "1" in line:
			containers = False

		line = line.strip('\n')

		if containers:
			temp_lst = []
			for i in range(0, len(line), 4):
				#print('line:',line[i:i+4])
				val = line[i:i+4].replace('[', '')
				val = val.replace(']', '')
				temp_lst.append(val)
			lst.append(temp_lst)
		else:
			if "move" in line:
				if re.findall(r'\d+', line) != []:
					sequence.append([int(x) for x in re.findall(r'\d+', line)])

	#print(lst)
	lst.reverse()
	#print(lst)

	for _ in lst[0]:
		stacks.append([])

	for row in lst:
		for col, box in enumerate(row):
			if box.strip(' ') == "":
				pass
			else:
				check = stacks[col].append(box.strip(' '))
				#print(check)
				#print(col, box)

	#for i in stacks:
		#print(i.stack)
	#print(sequence)
	input_vals = [stacks, sequence]
	return input_vals


def part1(input_vals):
	stacks = input_vals[0]
	seq = input_vals[1]

	for _, move in enumerate(seq):
		num_moves = move[0]
		loc_orig = move[1]
		loc_dest = move[2]

		#print(f"move #{_+1}\n", stacks)

		for i in range(num_moves):
			#print(f"submove #{i+1}")
			box = stacks[loc_orig-1].pop()
			stacks[loc_dest-1].append(box)
		#print(stacks)
		#print("--------------")

	output = ""

	for col in stacks:
		if len(col) != 0:
			output += col.pop()

	return output

def part2(input_vals):
	stacks = input_vals[0]
	seq = input_vals[1]

	for _, move in enumerate(seq):
		num_moves = move[0]
		loc_orig = move[1]
		loc_dest = move[2]


		boxes = []
		for i in range(num_moves):
			boxes.append(stacks[loc_orig-1].pop())
		boxes.reverse()
		stacks[loc_dest-1] += boxes
		#print(stacks)
		#print("--------------")

	output = ""

	for col in stacks:
		if len(col) != 0:
			output += col.pop()

	return output   

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
 
	
