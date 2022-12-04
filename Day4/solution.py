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
        assigments = line.strip().split(',')

        x = assigments[0].split('-')
        y = assigments[1].split('-')

        elf1 = list(range(int(x[0]), int(x[1])+1))
        elf2 = list(range(int(y[0]), int(y[1])+1))

        input_vals.append([elf1, elf2])

    return input_vals


def part1(input_vals):

    counter = 0

    for assignments in input_vals:
        elf1 = assignments[0]
        elf2 = assignments[1]

        if (set(elf1)&set(elf2) == set(elf1)) or (set(elf1)&set(elf2) == set(elf2)):
            counter += 1

    return counter

def part2(input_vals):

    counter = 0
    for assignments in input_vals:
        elf1 = assignments[0]
        elf2 = assignments[1]

        if set(elf1)&set(elf2) != set([]):
            counter += 1

    return counter

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
 
    