import sys
from pathlib import Path
import urllib.request as ul
import os

# if debugMode:
# 	print(bcolors.Warning+"[]DEBUG"+bcolors.ENDC)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

debugMode = False
home = str(Path.home())
# Get list of packages
lineList = [line.rstrip('\n') for line in open("package.txt")]

if "-d" in sys.argv:
	debugMode = True

if "search" == sys.argv[1]:
	for i in lineList:
		if debugMode:
			print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
		if sys.argv[2].lower() in i.split(";")[0].lower():
			name = i.split(";")[0]
			version = i.split(";")[1]
			auther = i.split(";")[2]
			description = i.split(";")[3]
			print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC,"	",bcolors.HEADER+version+bcolors.ENDC,"	",bcolors.OKBLUE+auther+bcolors.ENDC)
			print(description)

if "list" == sys.argv[1]:
	for i in lineList:
		if debugMode:
			print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
		name = i.split(";")[0]
		version = i.split(";")[1]
		auther = i.split(";")[2]
		description = i.split(";")[3]
		print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC,"	",bcolors.HEADER+version+bcolors.ENDC,"	",bcolors.OKBLUE+auther+bcolors.ENDC)
		print(description)

if "install" == sys.argv[1]:
	for i in lineList:
		temp = i.split(";")
		if sys.argv[2] == temp[0]:
			index = -1
			if not os.path.isdir(str(Path.home())+"/package"):
				os.mkdir(str(Path.home())+"/package", mode=0o777 )
				print (bcolors.WARNING+"[]dir made"+bcolors.ENDC)
			if debugMode:
				print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,temp[4].split("/"),str(index))
			ul.urlretrieve(temp[4], str(Path.home())+"/package/"+temp[4].split("/")[index])
