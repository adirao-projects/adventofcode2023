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

	all_bag_dict = {}
	for line in f:
		line = line.strip()
		id_, data =  line.split(': ')
		id_ = id_.split(' ')[1]
		data = data.split('; ')
		bags = []
		bag_dict = {'total': {
						'red':0,
						'blue':0,
						'green':0
					},}
		for i, dat in enumerate(data):
			i+=1
			bag_dict[str(i)] = {
				'red' : 0,
				'blue' : 0,
				'green' : 0,
			}

			bags.append(dat.split(', '))

		for i, bag in enumerate(bags):
			i+=1
			for cube_type in bag:
				cube_type = cube_type.split(' ')
				bag_dict[str(i)][cube_type[1]] += int(cube_type[0])
				bag_dict['total'][cube_type[1]] += int(cube_type[0])

		
		all_bag_dict[id_] = bag_dict

	return all_bag_dict


def part1(all_bag_dict):
	init_cond = {
		'red' : 12,
		'green' : 13,
		'blue': 14,
	}
	sum_id = 0
	for id_ in all_bag_dict:
		sum_id+=int(id_)
		for i in range(1, len(all_bag_dict[id_])):
			if all_bag_dict[id_][str(i)]['red'] > init_cond['red'] or \
			all_bag_dict[id_][str(i)]['green'] > init_cond['green'] or \
			all_bag_dict[id_][str(i)]['blue'] > init_cond['blue']:
				sum_id -= int(id_)
				break

	return sum_id

def part2(all_bag_dict):
	cube_power_sum = 0
	for id_ in all_bag_dict:
		max_red = 0
		max_green = 0
		max_blue = 0
		for i in range(1, len(all_bag_dict[id_])):
			if max_red < all_bag_dict[id_][str(i)]['red']:
				max_red = all_bag_dict[id_][str(i)]['red']
			if max_green < all_bag_dict[id_][str(i)]['green']:
				max_green = all_bag_dict[id_][str(i)]['green']
			if max_blue < all_bag_dict[id_][str(i)]['blue']:
				max_blue = all_bag_dict[id_][str(i)]['blue']
		cube_power_sum += max_red * max_green * max_blue

	return cube_power_sum  

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