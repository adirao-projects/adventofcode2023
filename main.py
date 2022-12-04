import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--Part", type=int, help = "Which Part", default=0)
parser.add_argument("-d", "--Day", type=int, help = "Which Day do you want to run?", default=0)
parser.add_argument("-t", "--Test", action="store_true", help = "Uses test inputs")
args = parser.parse_args()

if __name__ == "__main__":
	os.chdir(os.getcwd() + f'/Day{args.Day}/')

	if args.Test:
		os.system(f"python solution.py -p {args.Part} -t")

	else:
		os.system(f"python solution.py -p {args.Part}")