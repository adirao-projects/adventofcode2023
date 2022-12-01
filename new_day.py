import shutil
import os

day = int(input('Day:'))
try:
	shutil.copytree(os.getcwd()+'\\Day0 [TEMPLATE]',os.getcwd()+'\\Day{}'.format(day))
	print('Successful')
except Exception as e:
	print('Failure')
	print(e)
print('press enter to close')
input()