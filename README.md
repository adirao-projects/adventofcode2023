# [Advent of Code 2023](https://adventofcode.com/2023/)

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

## [Day 1](https://adventofcode.com/2023/day/1)

#### Part 1

I got off to a slow start this year, didn't attempt the question until mid day. The question itself was quite chill. I spent most of the time trying to understand how to use my code. Part 1 mainly just focused around checking for digits in strings. All I did was get every digit in the string, add them to a list, and then take the first and last values of that list to form the desired number.

```python
# Strips the input line for just the numeric digits
strip_line = [int(x) for x in list(line[0]) if x.isdigit()]
# Turns the digits to a string so I can make them into a single number
# Then turns them into integers to add them to the calibration value 
sum_calib_val += int(str(strip_line[0])+str(strip_line[-1]))



return max(cal_total)
```

#### Part 2

For part two, was more interesting. Originally, I had attempted to just make a dictionary with the numbers as words and their corresponding value then running a find and replace. HOWEVER, this didn't work because of instances were two numbers alphabetical representation shared a character. For example: $\texttt{eightwonine}$ has $\texttt{eight}$ and $\texttt{two}$ sharing a $\texttt{t}$. 

```python
numbers = {'one' : 1, 'two' : 2, 
            'three' : 3, 'four' : 4, 
            'five' : 5, 'six' : 6,
            'seven' : 7, 'eight' : 8,
            'nine' : 9, 'zero' : 0}
```

Therefore, the algorithm was modified. Two "crawler" methods were written to interpret the string piece by piece from either the left or right. The moment there was a string that contained one of the above numbers (spelled out) or an actual number (1,2,...) the crawler was stopped and that digit returned.

```python
def first_digit_crawler(line):
    word=''
    for char in line:
        if char.isdigit():
            return str(char)
        else:
            word+=char
            for num in numbers:
                if num in word:
                    return str(numbers[num])

def last_digit_crawler(line):
    word=''
    for char in line[::-1]:
        if char.isdigit():
            return str(char)
        else:
            word=char+word
            for num in numbers:
                if num in word:
                    return str(numbers[num])
```

These digits were then interepreted as a string and combined together to get the desired number.

```python
for line in inputs:    
    first = first_digit_crawler(line)
    last = last_digit_crawler(line)

    sum_calib_val += int(first + last)
```

*Note, this is not my actual implementation and may not properly run; if you want to see that code it's in the repo*

## [Day 2](https://adventofcode.com/2023/day/2)

#### Part 1

Not going to lie, I was a bit sloshed when I started this one and kind of misinterpreted the question. Regardless, I spent the majority of my time here on input processing. I essentially just parsed the data into a jsonlike object - there was probably a much better, simpler way of doing this but, like I said, I was kind of out of it.

```python
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
```

With this expertly parsed data, solving the question was super easy. I just set some initial conditions (as defined in the question) and checked if any of the bags violated those intial conditions

```python
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
```

#### Part 2

Part two was effectively the same. Notice that the minimum number of cubes is the **maximum number of cubes observed** in any given bag during a game. Therefore, we just keep track of the max for each cube type, calculate the power, and sum them into our running count for $\texttt{cube\_power}$

```python
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
```

I can definitely optimize this (especially with the number of repeated $\texttt{if}$ statements) but that's for another day. I have finals coming up and I have to prep.



## [Day 3](https://adventofcode.com/2023/day/3)

#### Part 1



#### Part 2
