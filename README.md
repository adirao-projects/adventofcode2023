# [Advent of Code 2022](https://adventofcode.com/2022/)
---

## Preliminary

Hi there, my name is Adi. I like doing the Advent of Code every year and this year I want to document my progress and thoughts on each problem here on this git repo!

----

## How to use my starter code

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
```
cd Day1
python solution.py -t -p 1
```

---

## [Day 1](https://adventofcode.com/2022/day/1)
---

## [Day 2](https://adventofcode.com/2022/day/2)
---
