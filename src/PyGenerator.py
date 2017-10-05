#!/usr/bin/python3.5

# -*-coding:ENCODAGE -*

import os
import time
import json
import sys

##read config file
configFile = open('./Cppconfig.json')
configData = json.load(configFile)

#get all important datas
typeGen = configData["type"]
nbrFile = int(configData["size"])
projectName = configData["name"]


#project creation
print("[info] création d'un projet en " + typeGen)
print("[info] " + str(nbrFile) + " fichiers demandés")
print("[Create] folder : " + projectName)

os.system("mkdir " + projectName)

#browse all file to make
i=0
while i<nbrFile:
	ptPy = projectName + "/" + configData["file"][str(i)]["name"]+".py"

	os.system("touch " + ptPy)

	#case usual fil
	if configData["file"][str(i)]["type"] == "casual" :
		os.system("cp ./templates/pyclasse.py " + ptPy)

	#case main just need a main()
	if configData["file"][str(i)]["type"] == "main" :
		os.system("cp ./templates/pyclasse.py " + ptPy)


	#case class
	if configData["file"][str(i)]["type"] == "class" :
		os.system("cp ./templates/pyclasse.py " + ptPy)
		pystr = "'\nclass " + configData["file"][str(i)]["name"] +" {\n\n	public :\n\n	private :\n\n};'";
		os.system("echo " + pystr + " >> " + ptPy)

	i=i+1

