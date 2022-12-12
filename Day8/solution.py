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
		temp = list(line.strip())
		temp = [int(x) for x in temp]
		input_vals.append(temp)

	return input_vals


def part1(input_vals):
	#print(input_vals)
	val_mat = np.array(input_vals)
	val_mat_r = np.flip(val_mat, axis=1)

	val_mat_t = np.transpose(val_mat)
	val_mat_r_t = np.flip(val_mat_t, axis=1)

	rows = len(input_vals)
	cols = len(input_vals[0])

	check_mat = np.ones((rows, cols), dtype=int)

	max_vals = []

	edge_count = 2*(rows + cols) - 4

	row_count = 1
	col_count = 1
	count = 0
	print("-------Normal-----\n", val_mat, "\n")
	print("-------Revers-----\n", val_mat_r, "\n")
	print("-------Transp-----\n", val_mat_t, "\n")
	print("-------TranRe-----\n", val_mat_r_t, "\n")
	#print(np.max(val_mat, axis=0))
	row_max = list(np.max(val_mat, axis=0))
	print(row_max)
	#print(np.max(val_mat_t, axis=0))
	col_max = list(np.max(val_mat_t, axis=0))
	print(col_max)

	cur_max = 0

	# Left to Right Check
	for r in range(1, rows - 1):
		#Itterating through target rows

		row = val_mat[r]
		max_val = 0
		max_val = val_mat[r][0]
		for c in range(1, cols - 1):
			tree = val_mat[r][c]
			max_val = max([max_val, val_mat[r][c-1]])
			#print(tree)
			if (((tree)*(check_mat[r][c]))>max_val):
				count += 1
				check_mat[r][c] = 0

	#print(check_mat)
	# Right to Left Check
	check_mat = np.flip(check_mat, axis=1)
	for r in range(1, rows - 1):
		#Itterating through target rows

		row = val_mat_r[r]
		max_val = val_mat_r[r][0]
		for c in range(1, cols - 1):

			tree = val_mat_r[r][c]
			#print(tree)
			max_val = max([max_val, val_mat_r[r][c-1]])
			#print(tree)
			if (((tree)*(check_mat[r][c]))>max_val):
				count += 1
				check_mat[r][c] = 0

	# Up to Down Check
	check_mat = np.flip(check_mat, axis=1)
	check_mat = np.transpose(check_mat)
	for r in range(1, rows - 1):
		#Itterating through target cols

		row = val_mat_t[r]
		max_val = val_mat_t[r][0]
		for c in range(1, cols - 1):
			tree = val_mat_t[r][c]
			#print(tree)
			max_val = max([max_val, val_mat_t[r][c-1]])
			#print(tree)
			if (((tree)*(check_mat[r][c]))>max_val):
				count += 1
				check_mat[r][c] = 0


	check_mat = np.flip(check_mat, axis=1)
	for r in range(1, rows - 1):
		#Itterating through target cols

		row = val_mat_r_t[r]
		max_val = val_mat_r_t[r][0]
		for c in range(1, cols - 1):
			tree = val_mat_r_t[r][c]
			max_val = max([max_val, val_mat_r_t[r][c-1]])
			#print(tree)
			if (((tree)*(check_mat[r][c]))>max_val):
				count += 1
				check_mat[r][c] = 0

	check_mat = np.flip(check_mat, axis=1)
	check_mat = np.transpose(check_mat)
	#print(check_mat)
	#print(val_mat_r_t)
	"""
	for r in range(1, rows - 1):
		# Itterate through rows twice (left-right)
		for c in range(1, cols - 1):
			if (val_mat[r][c] != row_max[r]) and (val_mat[r][c] > val_mat[r][c-1]):
				count += 1
			elif val_mat[r][c] == row_max[r]:
				break

		for c in range(1, cols - 1):
			if (val_mat_r[r][c] != row_max[r]) and (val_mat_r[r][c] > val_mat_r[r][c-1]):
				count += 1
			elif val_mat_r[r][c] == row_max[r]:
				break

	for c in range(1, cols - 1):
		for r in range(1, rows - 1):
			if (val_mat_t[c][r] != col_max[c]) and (val_mat[c][r] > val_mat[c][r-1]):
				count += 1
			elif val_mat[r][c] == row_max[r]:
				break

		for r in range(1, rows - 1):
			if (val_mat_r_t[r][c] != row_max[r]) and (val_mat_r_t[c][r] > val_mat_r_t[c][r-1]):
				count += 1
			elif val_mat_r_t[r][c] == row_max[r]:
				break
	"""

	return count+edge_count # count+edge_count - 1

def check_dir(loc, mat):
	loc_r = loc[0]
	loc_c = loc[1]

	scores = [0, 0, 0, 0]
	stop = [0, 0, 0, 0]

	while sum(stop)<4:
		# Check Up
		tar_r = loc_r - 1
		tar_c = loc_c
		if tar_r >= 0:	
			if mat[loc_r][loc_c]>mat[tar_r][tar_c]:
				scores[0] += 1
			else:
				stop[0] = 1
		else:
			stop[0] = 1

		# Check Down
		tar_r = loc_r + 1
		tar_c = loc_c
		if tar_r >= 0:	
			if mat[loc_r][loc_c]>mat[tar_r][tar_c]:
				scores[1] += 1
			else:
				stop[1] = 1
		else:
			stop[1] = 1

		# Check Left
		tar_r = loc_r
		tar_c = loc_c - 1
		if tar_r >= 0:	
			if mat[loc_r][loc_c]>mat[tar_r][tar_c]:
				scores[2] += 1
			else:
				stop[2] = 1
		else:
			stop[2] = 1

		# Check Right
		tar_r = loc_r
		tar_c = loc_c + 1
		if tar_r >= 0:	
			if mat[loc_r][loc_c]>mat[tar_r][tar_c]:
				scores[3] += 1
			else:
				stop[3] = 1
		else:
			stop[3] = 1

	return scores

def part2(input_vals):
	val_mat = np.array(input_vals)
	rows = len(input_vals)
	cols = len(input_vals[0])
	up_sc = 0
	down_sc = 0 
	righ_sc = 0
	left_sc = 0

	# Left to Right Check
	for r in range(1, rows - 1):
		#Itterating through target rows

		for c in range(1, cols - 1):
			tree = val_mat[r][c]
			temp =  check_dir((r,c), val_mat)
			score = temp[0]*temp[1]*temp[2]*temp[3]
			senic_scores.append(score)

			#max_val = max([max_val, val_mat[r][c-1]])

			#if (((tree)*(check_mat[r][c]))>max_val):
			#	count += 1
			#	check_mat[r][c] = 0

	"""
				#print(check_mat)
				# Right to Left Check
				check_mat = np.flip(check_mat, axis=1)
				for r in range(1, rows - 1):
					#Itterating through target rows
			
					row = val_mat_r[r]
					max_val = val_mat_r[r][0]
					for c in range(1, cols - 1):
			
						tree = val_mat_r[r][c]
			
						max_val = max([max_val, val_mat_r[r][c-1]])
			
						if (((tree)*(check_mat[r][c]))>max_val):
							count += 1
							check_mat[r][c] = 0
			
				# Up to Down Check
				check_mat = np.flip(check_mat, axis=1)
				check_mat = np.transpose(check_mat)
				for r in range(1, rows - 1):
					#Itterating through target cols
			
					row = val_mat_t[r]
					max_val = val_mat_t[r][0]
					for c in range(1, cols - 1):
						tree = val_mat_t[r][c]
			
						max_val = max([max_val, val_mat_t[r][c-1]])
			
						if (((tree)*(check_mat[r][c]))>max_val):
							count += 1
							check_mat[r][c] = 0
			
			
				check_mat = np.flip(check_mat, axis=1)
				for r in range(1, rows - 1):
					#Itterating through target cols
			
					row = val_mat_r_t[r]
					max_val = val_mat_r_t[r][0]
					for c in range(1, cols - 1):
						tree = val_mat_r_t[r][c]
						max_val = max([max_val, val_mat_r_t[r][c-1]])
			
						if (((tree)*(check_mat[r][c]))>max_val):
							count += 1
							check_mat[r][c] = 0
			
				check_mat = np.flip(check_mat, axis=1)
				check_mat = np.transpose(check_mat)
	"""
	#print(check_mat)
	#print(val_mat_r_t)
	"""
	for r in range(1, rows - 1):
		# Itterate through rows twice (left-right)
		for c in range(1, cols - 1):
			if (val_mat[r][c] != row_max[r]) and (val_mat[r][c] > val_mat[r][c-1]):
				count += 1
			elif val_mat[r][c] == row_max[r]:
				break

		for c in range(1, cols - 1):
			if (val_mat_r[r][c] != row_max[r]) and (val_mat_r[r][c] > val_mat_r[r][c-1]):
				count += 1
			elif val_mat_r[r][c] == row_max[r]:
				break

	for c in range(1, cols - 1):
		for r in range(1, rows - 1):
			if (val_mat_t[c][r] != col_max[c]) and (val_mat[c][r] > val_mat[c][r-1]):
				count += 1
			elif val_mat[r][c] == row_max[r]:
				break

		for r in range(1, rows - 1):
			if (val_mat_r_t[r][c] != row_max[r]) and (val_mat_r_t[c][r] > val_mat_r_t[c][r-1]):
				count += 1
			elif val_mat_r_t[r][c] == row_max[r]:
				break
	"""

	return max(senic_scores) # count+edge_count - 1 

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
	