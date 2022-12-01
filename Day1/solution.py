import numpy as np
from itertools import combinations

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Part", type=int, help = "Which Part", default=0)
parser.add_argument("-t", "--Test", action="store_true", help = "Uses test inputs")
args = parser.parse_args()

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
    inputs = []
    for line in f:
        try:
            inputs.append([int(x) for x in line.strip().split(' ')][0])
        except:
            input_vals.append(inputs)
            inputs = []

    return input_vals


def part1(input_vals):
    elf_cal = []

    for elf, elf_food in enumerate(input_vals):
        elf_cal.append(sum(elf_food))

    elf_most = elf_cal.index(max(elf_cal))+1
    elf_most_cal = max(elf_cal)

    return elf_most, elf_most_cal

def find_max(lst):

    elf_most = lst.index(max(lst))+1
    elf_most_cal = max(lst)

    return elf_most, elf_most_cal

def part2(input_vals):
    top_three_elf = []
    top_three_cal = []
    elf_cal = []

    for elf, elf_food in enumerate(input_vals):
        elf_cal.append(sum(elf_food))

    elf1, cal1 = find_max(elf_cal)
    elf_cal.remove(cal1)

    elf2, cal2 = find_max(elf_cal)
    elf_cal.remove(cal2)

    elf3, cal3 = find_max(elf_cal)
    elf_cal.remove(cal3)

    elf_most = elf_cal.index(max(elf_cal))+1
    elf_most_cal = max(elf_cal)

    output = cal1+cal2+cal3

    return output

def optimized(input_vals, num_max=1):
    top_elfs = []
    top_cals = []
    elf_cal = []

    for elf, elf_food in enumerate(input_vals):
        elf_cal.append(sum(elf_food))

    for i in range(num_max):
        max_vals = find_max(elf_cal)[1]

        top_elds.append(max_vals[0])
        top_cals.append(max_vals[1])

        elf_cal.remove(elf_cal[1])

    output = sum(top_cals)
    
    return output

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
 
    