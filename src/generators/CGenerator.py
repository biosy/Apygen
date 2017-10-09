#!/usr/bin/python3.5
# -*-coding:utf-8 -*

import os
import time
import json
import sys


##read config file
configFile = open('./config.json')
configData = json.load(configFile)

#get all important datas
typeGen = configData["type"]
nbrFile = int(configData["size"])
projectName = configData["name"]


#project creation
print(str("[info] création d'un projet en " + typeGen))
print("[info] " + str(nbrFile) + " fichiers demandés")
print("[Create] folder : " + projectName)

os.system("mkdir " + projectName)

#browse all file to make
i=0
while i<nbrFile:
	ptC = projectName + "/" + configData["file"][str(i)]["name"]+".c"
	ptH = projectName + "/" + configData["file"][str(i)]["name"]+".h"
	includer = "\42" + configData["file"][str(i)]["name"]+".h\42"

	os.system("touch " + ptC)

	#case usual file, need a .h
	if configData["file"][str(i)]["type"] == "casual" :
		os.system("cp ../templates/ptH.h " + ptH)
		os.system("echo '\43include "+includer+"' >> " + ptC)
		print("[Create] file : " + ptH)

	#case main just need a main()
	if configData["file"][str(i)]["type"] == "main" :
		os.system("cp ../templates/main.c " + ptC)

	i = i+1

	#generate a generic makefile
	os.system("cp ../templates/Makefile "+ projectName)

