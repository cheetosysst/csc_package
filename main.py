import sys
import os
import urllib.request as ul
# Variable


# Get list of packages
lineList = [line.rstrip('\n') for line in open("package.txt")]

if "search" == sys.argv[1]:
	print (sys.argv[2])

if "install" == sys.argv[1]:
	for i in lineList:
		temp = i.split(";")
		if sys.argv[2] == temp[0]:
			ul.urlretrieve(temp[4], "./example.txt")