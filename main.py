import sys
from pathlib import Path
import urllib.request as ul
import os
import subprocess as sp

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
lineList = [line.rstrip('\n') for line in open("package.txt")]

if "-d" in sys.argv:
	debugMode = True

if "update" == sys.argv[1]:
	print("Updating " + bcolors.WARNING + "package.txt" + bcolors.ENDC)
	# download from server
	print("Finish Downloading, type" + bcolors.WARNING + " \"csc upgradable\" " + bcolors.ENDC + "for updatable packages")
	exit()

if "show" == sys.argv[1]:
	packageName = sys.argv[2]
	for i in lineList:
		if i.split(";")[0].lower() == packageName.lower():
			name = i.split(";")[0]
			version = i.split(";")[1]
			auther = i.split(";")[2]
			description = i.split(";")[3]
			print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
			print(description)
	exit()

if "search" == sys.argv[1]:
	for i in lineList:
		if debugMode:
			print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
		if sys.argv[2].lower() in i.split(";")[0].lower():
			name = i.split(";")[0]
			version = i.split(";")[1]
			auther = i.split(";")[2]
			description = i.split(";")[3]
			print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
			print(description)
	exit()

if "list" == sys.argv[1]:
	for i in lineList:
		if debugMode:
			print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
		name = i.split(";")[0]
		version = i.split(";")[1]
		auther = i.split(";")[2]
		description = i.split(";")[3]
		print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
		print(description)
	exit()

if "install" == sys.argv[1]:
	for i in lineList:
		temp = i.split(";")
		if sys.argv[2].lower() == temp[0].lower():
			index = -1
			name = i.split(";")[0]
			if not os.path.isdir(str(Path.home())+"/package"):
				os.mkdir(str(Path.home())+"/package", mode=0o777 )
				print (bcolors.WARNING+"[]dir made"+bcolors.ENDC)
			if debugMode:
				print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,temp[4].split("/"),str(index))
			print("Downloading package "+bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+" ...")
			ul.urlretrieve(temp[4], str(Path.home())+"/package/"+temp[4].split("/")[index])
			print("Extracting package ...")
			if debugMode:
				print(["tar" ,"-xf" ,str(Path.home())+"/package/"+temp[4].split("/")[index] ,str(Path.home())+"/package"])
			sp.run(["tar" ,"-xf" ,str(Path.home())+"/package/"+temp[4].split("/")[index] ,"--directory="+str(Path.home())+"/package"])
			print("Removing tar file")
			os.remove(str(Path.home())+"/package/"+temp[4].split("/")[index])
			print("Checking if make  config exist")
			if temp[5] == "none":
				print ("Config file not found, proceed to default install")
			else:
				print("Config file found at " ,bcolors.WARNING + temp[5]+bcolors.ENDC,", downloading ...")
