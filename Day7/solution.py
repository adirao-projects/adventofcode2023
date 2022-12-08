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
    	input_vals.append(line.strip())

    return input_vals


def part1(input_vals):
	#print(input_vals)
	line_count = 0
	cur_dir_lst = []
	cur_dir = ""
	data_dict = {}
	size = 0

	for line in input_vals:
		if "$" in line and "cd" in line:
			if line.split(" ")[2] == "..":
				cur_dir_lst.pop()
			else:
				cur_dir_lst.append(line.split(" ")[2])
				cur_dir = ''.join(cur_dir_lst)
				data_dict[cur_dir] = 0

		elif "$" in line and "ls" in line:
			pass

		else:
			if "dir" not in line:
				size = int(line.split(" ")[0])
				search_str = ""
				for char in cur_dir_lst:
					search_str = search_str + char
					data_dict[search_str] += size


	output = 0
	for val in data_dict.values():
		if val <= 100000:
			output+=val
	return output


def part2(input_vals):

	line_count = 0
	cur_dir_lst = []
	cur_dir = ""
	data_dict = {}
	size = 0

	for line in input_vals:
		if "$" in line and "cd" in line:
			if line.split(" ")[2] == "..":
				cur_dir_lst.pop()
			else:
				cur_dir_lst.append(line.split(" ")[2])
				cur_dir = ''.join(cur_dir_lst)
				data_dict[cur_dir] = 0

		elif "$" in line and "ls" in line:
			pass

		else:
			if "dir" not in line:
				size = int(line.split(" ")[0])
				search_str = ""
				for char in cur_dir_lst:
					search_str = search_str + char
					data_dict[search_str] += size


	#output = 0
	valid = []
	for val in data_dict.values():
		if val >= (30000000-(70000000-data_dict["/"])):
			valid.append(val)

	return min(valid)

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
 
    