import shutil
#import os
#import argparse
#import sys
#import Algorithms
#import ComplexDataStructures



day = int(input('Day:'))

try:
	shutil.copytree(os.getcwd()+'\\Day0 [TEMPLATE]',os.getcwd()+'\\Day{}'.format(day))
	print('Folder creation successful')
except Exception as e:
	print('Failure')
	print(e)
print('press enter to close')
input()