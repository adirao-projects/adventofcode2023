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
        string = list(line.strip())
        mid = len(string)//2
        input_vals.append([string[:mid], string[mid:]])

    return input_vals

alphabet = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4, 
    'e' : 5, 
    'f' : 6, 
    'g' : 7, 
    'h' : 8, 
    'i' : 9, 
    'j' : 10, 
    'k' : 11, 
    'l' : 12,
    'm' : 13,
    'n' : 14,
    'o' : 15,
    'p' : 16,
    'q' : 17,
    'r' : 18,
    's' : 19,
    't' : 20,
    'u' : 21,
    'v' : 22,
    'w' : 23,
    'x' : 24,
    'y' : 25,
    'z' : 26,
    'A' : 27,
    'B' : 28,
    'C' : 29,
    'D' : 30,
    'E' : 31,
    'F' : 32,
    'G' : 33,
    'H' : 34,
    'I' : 35,
    'J' : 36,
    'K' : 37,
    'L' : 38,
    'M' : 39,
    'N' : 40,
    'O' : 41,
    'P' : 42,
    'Q' : 43,
    'R' : 44,
    'S' : 45,
    'T' : 46,
    'U' : 47,
    'V' : 48,
    'W' : 49,
    'X' : 50,
    'Y' : 51,
    'Z' : 52
    }

def alphabet_value(alpha):
    if alpha.isupper():
        return ord(alpha.lower()) - 96 + 26
    else:
        return ord(alpha)-96

def part1(input_vals):
    priority = []
    output = 0
    #print(input_vals)
    for ruck in input_vals:
        common_set = {x for x in ruck[0] if (x in ruck[1])}
        priority += list(common_set)


    #print(priority)
    for i in priority:
        #print(f"{i} : {alphabet_value(i)}")
        output += alphabet_value(i)

    return output

def part2(input_vals):
    priority = []
    output = 0
    rucklist = []
    #print(input_vals)
    for i, ruck in enumerate(input_vals):
        rucklist.append(ruck[0]+ruck[1])
        #print(i, ruck)
        if (i+1)%3 == 0:
            #print(rucks)
            common_set = set(rucklist[i-2]) & set(rucklist[i-1]) & set(rucklist[i])
            #print(common_set)
            priority += list(common_set)

    for i in priority:
        #print(i)
        #print(f"{i} : {alphabet_value(i)}")
        output += alphabet_value(i)

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
 
    