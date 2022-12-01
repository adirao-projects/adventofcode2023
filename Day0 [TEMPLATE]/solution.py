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
        input_vals.append([int(x) for x in line.strip().split(' ')])

    return input_vals


def part1(input_vals):
	output = None
    pass
    return output

def part2(input_vals):
	output = None
    pass
    return output

def optimized(input_vals):
    output = None
    pass
    return output

if __name__=="__main__": 
    f = openFile(True)    
    input_vals = inputProcess(f)
    
    output = None
    #output = part1(input_vals)
    #output = part2(input_vals) 
  	#output = optimized(input_vals)
    
    print(output)
 
    