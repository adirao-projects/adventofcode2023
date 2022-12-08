# [Advent of Code 2022](https://adventofcode.com/2022/)

---

## Forward

Hi there, my name is Adi. I like doing the Advent of Code every year and this year I want to document my progress and thoughts on each problem here on this git repo. I'm [@adiraowastaken on Twitter](https://twitter.com/adiraowastaken) and I should be posting there to. Edits are welcome (especially to the starter files), just create a pull request before you do anything.



**IMPORTANT, there are solutions that are posted here so don't spoil yourself!**



----

## How to use my starter code

### Running Files

In the file you'll find a python file called `new_day.py` this creates a copy of the Day template file onto your computer to prep you for the next day of the calendar (useful when you're racing to get one of the first 200 stars). To run the code, argparser has been added to run everything directly from the commandline

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Part", type=int, help = "Which Part", 
                    default=0)
parser.add_argument("-t", "--Test", action="store_true", 
                    help = "Uses test inputs")
args = parser.parse_args()
```

Depending on which part of the question you're doing (Part 1 or 2) pass the desired number. If you want to run your test inputs from the `test_inputs.txt` pass the `-t` arguement. 

You ideally want to write in the `inputProcess` file first to parse your inputs, some starter functions have been included (more may be added later depending on how much utility they add).

Next work on `part1` and subsequently `part2`, and then - if you care to - you can optimize your solution after (assuming you were just hacking together something as fast as possible). 

For example, the following would run day 1 part 1 in test mode:

```bash
cd Day1
python solution.py -t -p 1
```

Alternatively, you can run everything from the parent directory by calling `main.py` and passing the `-d` argumentent following by an integer for day number. To run day 1 part 2 in test mode it would be the following:

```bash
python main.py -d 1 -p 2 -t 
```

### Helper Files

There are also a few helper files included with the starter code. This includes useful algorithms and datastructures that you might need (but might not have the time to write from scratch). If you need to change anything, it is advised that you overload the class in order to preserve the classes for later use on other days. All the files should be fully type annotated with information about any algorithms.

#### Algorithms

The algorithms file `UsefulAlgorithms.py` included may not all be implemented (are being updated everyday). There are quite a few (add a pull request if you want to add another). Here are the ones I've added so far:

- [x] Binary Search

- [ ] Tenary Search

- [ ] Quick Sort

- [x] Merge Sort

- [ ] Rabin-Karp

- [ ] KMP

Many of the algorithms are being referenced from [here](https://codeofgeeks.com/important-algorithms-for-competitive-programming) and some of the starter code is taken and or referenced from [geeksforgeeks](https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/). I may add more later!

#### DataStructures

The datastructures file `ComplexDataStructures.py` includes lesser used more specalized datastrutures. These include the following

- [x] Single Linked List

- [ ] Double Linked List

- [x] Hashmap

- [x] Trees

- [ ] BinaryTrees

- [x] Stack

- [x] Queue

Most of these are written by me and a lot are being updated and refactored with better implementations more comments and improved documentation.

---

## [Day 1](https://adventofcode.com/2022/day/1)

Day one so far was not too bad at all, got off to a bit of a slow start reading the question but in terms of actual implementation there wasn't too much to it. 

I simply did the following: Add up all the calories, add them to a list, and return the max value.

```python
all_cals = [[1000, 2000, 3000], 
            [4000], 
            [5000, 6000], 
            [7000, 8000, 9000], 
            [10000]]

cal_total = []
for i in all_cals:
    cal_total.append(sum(i))


return max(cal_total)
```

For part two, I changed it slightly, simply popping the two value out of the list and refinding the max.

```python
all_cals = [[1000, 2000, 3000], 
            [4000], 
            [5000, 6000], 
            [7000, 8000, 9000], 
            [10000]]

cal_total = []
for i in all_cals:
    cal_total.append(sum(i))

sum_val = 0
for i in range(3):
    sum_val += max(cal_total)
    cal_total.remove(max(cal_total))


return sum_val
```

*Note, this is not my actual implementation and may not properly run; if you want to see that code it's in the repo*

---

## [Day 2](https://adventofcode.com/2022/day/2)

---

## [Day 3](https://adventofcode.com/2022/day/3)

---

## [Day 4](https://adventofcode.com/2022/day/4)

---
