#!/usr/bin/python3

import os 

FILE_NAME  = "/home/ch3/not_the_flag"

try :
	with open(FILE_NAME) as f :
		print(f.read())
	os.remove(FILE_NAME)
except Exception as e :
	print(e)