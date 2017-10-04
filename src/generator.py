#!/usr/bin/python3.5

# -*-coding:ENCODAGE -*

import os
import time
import json

##read config file
configFile = open('./config.json')
configData = json.load(configFile)

#get all important datas
typeGen = configData["type"]
nbrFile = int(configData["size"])
projectName = configData["name"]

print("[info] création d'un projet en " + typeGen)
print("[info] " + str(nbrFile) + " fichiers demandés")

i=0
print("[Create] folder : " + projectName)

os.system("mkdir " + projectName)

while i<nbrFile:
	ptC = projectName + "/" + configData["file"][str(i)]["name"]+".c"
	ptH = projectName + "/" + configData["file"][str(i)]["name"]+".h"
	os.system("touch " + ptC)
	if configData["file"][str(i)]["type"] == "casual" :
		os.system("touch " + ptH)
		print("[Create] file : " + ptH)

	print("[Create] file : " + ptC)

	i = i+1

##### case C #####

# generate Makefile

# create all files

# fill with some shitty stuff


##### case C++ ######

# generate Makefile

# create all files

# fill files with some shitty stuff


##### case python #####

# create all files

# full files with some shitty stuff TOTO : class


##### TODO : add more langages like : 
	## java
	## C#

##### add the possibility to put some documentations with templates


##### more features
