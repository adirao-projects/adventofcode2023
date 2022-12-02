import argparse

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
        input_vals.append(line.strip().split(' '))

    return input_vals


def part1(input_vals):
    scores = {  "A": 1,
                "B": 2,
                "C": 3,
                "X": 1, 
                "Y": 2,
                "Z": 3}
    tot_score = 0
    for opp, ply in input_vals:
        tot_score += scores[ply]
        if scores[opp]==scores[ply]:
            tot_score += 3

        elif scores[opp]==3 and scores[ply]==1:
            tot_score += 6

        elif scores[opp]==1 and scores[ply]==3:
            tot_score += 0

        elif scores[opp]>scores[ply]:
            tot_score += 0

        elif scores[opp]<scores[ply]:
            tot_score += 6

        


    return tot_score

def part2(input_vals):
    score_opts = [1, 2, 3]
    scores = {  "A": 1,
                "B": 2,
                "C": 3,
            }
    tot_score = 0
    for opp, outcome in input_vals:
        if outcome=="X":
            desired = score_opts.index(scores[opp]) - 1
            tot_score +=0
            tot_score += score_opts[desired]

        elif outcome=="Y":
            desired = score_opts.index(scores[opp])
            tot_score +=3
            tot_score += score_opts[desired]

        elif outcome=="Z":
            desired = (score_opts.index(scores[opp]) + 1)%3
            tot_score += 6
            tot_score += score_opts[desired]

    return tot_score

def optimized(input_vals):
    pass

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
 
    