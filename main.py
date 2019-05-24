# Import module
import sys
from pathlib import Path
import urllib.request as ul
import os
import subprocess as sp

# Class for text colors
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Variable and data
debugMode = False
home = str(Path.home())
lineList = [line.rstrip('\n') for line in open("package.txt")]

if len(sys.argv) < 2:
	print("Please specify task") 
	exit()

# Debug mode: If "-d" is in sys.argv debugMode set to true
if "-d" in sys.argv:
	print(bcolors.FAIL+"[] Debug mode enable"+bcolors.ENDC) # It doesn't work, tre to fix it in the future
	debugMode = True

# Help mode: Print out useful content on how to use the software
if "help" == sys.argv[1] or "-h" in sys.argv:
	if debugMode:
		print(bcolors.HEADER+"[] Help mode start"+bcolors.ENDC)
	print(bcolors.HEADER+bcolors.BOLD+"Usage : csc <method> <string> <debug : -d>"+bcolors.ENDC)
	print(bcolors.BOLD+"Method:"+bcolors.ENDC)
	print(bcolors.WARNING+"	install	"+bcolors.ENDC+"Install packages, currently one at a time.")
	print(bcolors.WARNING+"	show	"+bcolors.ENDC+"Display description of certain package.")
	print(bcolors.WARNING+"	list	"+bcolors.ENDC+"List all avalible package description.")
	print(bcolors.WARNING+"	search	"+bcolors.ENDC+"Search for packages.")
	print(bcolors.WARNING+"	update	"+bcolors.ENDC+"Update package list from the internet.")
	print(bcolors.BOLD+"Arguments:"+bcolors.ENDC)
	print(bcolors.WARNING+"	-d	"+bcolors.ENDC+"Enable debug mode, which display where the program is currently running.")
	print("See more on github page, https://github.com/cheetosysst/csc_package")
	if debugMode:
		print(bcolors.HEADER+"[] Help mode exit"+bcolors.ENDC)
	exit()

# Update mode
if "update" == sys.argv[1]:
	if debugMode:
		print(bcolors.HEADER+"[] Update mode start"+bcolors.ENDC)
	print("Updating " + bcolors.WARNING + "package.txt" + bcolors.ENDC)
	# download from server, currently empty. I'll update it when I have a online server somwhere
	print("Finish Downloading, type" + bcolors.WARNING + " \"csc upgradable\" " + bcolors.ENDC + "for upgradable packages")
	if debugMode:
		print(bcolors.HEADER+"[] Update mode exit"+bcolors.ENDC)
	exit()

# Show mode
if "show" == sys.argv[1]:
	if debugMode:
		print(bcolors.HEADER+"[] Show mode start"+bcolors.ENDC)
	if len(sys.argv) < 3: # Check if package name is specified
		print("Please specify the package name")
	else:
		packageName = sys.argv[2]
		found =False
		for i in lineList:
			if i.split(";")[0].lower() == packageName.lower():
				found = True
				# Gather data
				name = i.split(";")[0]
				version = i.split(";")[1]
				auther = i.split(";")[2]
				description = i.split(";")[3]
				# Print data
				print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
				print(description)
		if not found:
			print("Package not found, please use search or update the package list")
	if debugMode:
		print(bcolors.HEADER+"[] Show mode exit"+bcolors.ENDC)
	exit()

# Search mode
if "search" == sys.argv[1]:
	if debugMode:
		print(bcolors.HEADER+"[] Search mode start"+bcolors.ENDC)
	if len(sys.argv) < 3:
		print("Please specify package name")
	else:
		for i in lineList:
			if debugMode:
				print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
			if sys.argv[2].lower() in i.split(";")[0].lower():
				# Data gathering
				name = i.split(";")[0]
				version = i.split(";")[1]
				auther = i.split(";")[2]
				description = i.split(";")[3]
				# Print out data
				print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
				print(description)
		if debugMode:
			print(bcolors.HEADER+"[] Search mode start"+bcolors.ENDC)
	exit()

# List mode
if "list" == sys.argv[1]:
	if debugMode:
		print(bcolors.HEADER+"[] List mode start"+bcolors.ENDC)
	for i in lineList:
		if i == "": # Prevent crash cause by empty line
			break
		if debugMode:
			print(bcolors.WARNING+"[]DEBUG"+bcolors.ENDC,i)
		# Data gathering
		name = i.split(";")[0]
		version = i.split(";")[1]
		auther = i.split(";")[2]
		description = i.split(";")[3]
		# Print out data
		print(bcolors.WARNING+bcolors.BOLD+name+bcolors.ENDC+"	"+bcolors.HEADER+version+bcolors.ENDC+"	"+bcolors.OKBLUE+auther+bcolors.ENDC)
		print(description)
	if debugMode:
		print(bcolors.HEADER+"[] List mode exit"+bcolors.ENDC)
	exit()

# Install mode
if "install" == sys.argv[1]:
	if debugMode:
		print(bcolors.HEADER+"[] Install mode start"+bcolors.ENDC)
	if len(sys.argv) < 3:
		print("Please specify the package name")
	else:
		found = False
		for i in lineList:
			temp = i.split(";")
			if sys.argv[2].lower() == temp[0].lower():
				found = True
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
					print(bcolors.WARNING+"[] Debug"+bcolors.ENDC,["tar" ,"-xf" ,str(Path.home())+"/package/"+temp[4].split("/")[index] ,str(Path.home())+"/package"])
				sp.run(["tar" ,"-xf" ,str(Path.home())+"/package/"+temp[4].split("/")[index] ,"--directory="+str(Path.home())+"/package"])
				print("Removing tar file")
				os.remove(str(Path.home())+"/package/"+temp[4].split("/")[index])
				print("Checking if make  config exist")
				if temp[5] == "none":
					print ("Config file not found, proceed to default install")
				else:
					print("Config file found at " ,bcolors.WARNING + temp[5]+bcolors.ENDC,", downloading ...")
		if not found:
				print("Package not found, try updating the package list or run search to check the name of the package.")

		if debugMode:
			print(bcolors.HEADER+"[] Install mode exit"+bcolors.ENDC)
	exit()
