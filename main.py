import sys
from pathlib import Path
import urllib.request as ul
import os
# Variable

home = str(Path.home())
# Get list of packages
lineList = [line.rstrip('\n') for line in open("package.txt")]

if "search" == sys.argv[1]:
	print (sys.argv[2])

if "install" == sys.argv[1]:
	for i in lineList:
		temp = i.split(";")
		if sys.argv[2] == temp[0]:
			if not os.path.isdir(str(Path.home())+"/package"):
				os.mkdir(str(Path.home())+"/package", mode=0o777 )
				print ("dir made")
			print(str(Path.home())+"/package/"+temp[4].split("/")[len(temp)-1])
			ul.urlretrieve(temp[4], str(Path.home())+"/package/"+temp[4].split("/")[len(temp)-1])
