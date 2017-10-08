#!/usr/bin/python3.5

# -*-coding:ENCODAGE -*

import os
import time
import json
import sys
import string

flag = True
auto = 0

while flag :


	choice  = input("> ")
	file = ""
	prname = ""

	if(choice == "create project") :
		print("select a name")
		name  = input("	> ")
		print("select a langage")
		langage  = input("	> ")
		while ((langage != "C") and (langage != "Python")and(langage != "C++")):
			print("project type must be C++, C or Python")
			langage  = input("       > ")

		os.system("touch ./config/" + name + ".json")
		os.system("cp ./templates/config.json ./config/" + name +".json")
		auto=1

		config = open("config/"+name +".json","r+")
		dataConfig = json.load(config)
		dataConfig["size"] = "0"
		dataConfig["name"] = name
		dataConfig["type"] = langage
		dataConfig["file"] = {}
		output = open("config/"+name + ".json", "w")
		output.write(json.dumps(dataConfig, indent = 4))
		os.system("echo '"+ name+"' >> config/list.json")
		output.close()
		auto = 2

	elif(choice == "ls project"):
		os.system("cat ./config/list.json")

	elif(choice == "exit"):
		quit()

	elif(choice == "add"):
		print("select project name")
		prname = input("	 > ")
		while not (os.path.exists("./config/" + prname + ".json")):
			print("not a valid project")
			prname = input("	> ")

		while(file != "ok"):
			print("select file to add")
			file = input("	>")
			jsonfile = open("config/"+prname+".json", "r+")
			jsondata = json.load(jsonfile)
			jsondata["file"][file]={}
			type = jsondata["type"]
			jsonfile.close()
			output = open("config/"+prname+".json", "r+")
			output.write(json.dumps(jsondata, indent = 4))
			output.close()
			jsonfile = open("config/"+prname+".json", "r+")
			jsondata = json.load(jsonfile)
			jsondata["file"][file]["name"] = file

			if(type == "C"):
				type_file = input( "choose a type of file : c for casual or m for main ")
				while(type_file!="c" and type_file != "m"):
					type_file = input("not a good choice ")

				if(type_file =="c"):
					jsondata["file"][file]["type"] = "casual"

				if(type_file =="m"):
					jsondata["file"][file]["type"] = "main"


			if(type == "C++" or type == "Python"):
				type_file = input( "choose a type of file : c for casual or m for main or cp for class ")
				while(type_file!="c" and type_file != "m" and type_file !="cp"):
					type_file = input("not a good choice ")

				if(type_file =="c"):
					jsondata["file"][file]["type"] = "casual"

				if(type_file =="m"):
					jsondata["file"][file]["type"] = "main"

				if(type_file =="cp"):
					jsondata["file"][file]["type"] = "class"


			size = int(jsondata["size"])
			jsondata["size"] = str(size+1)
			output = open("config/"+prname+".json", "w+")
			output.write(json.dumps(jsondata, indent = 4))
			output.close()

	elif(choice == "generate"):
		print("select project name")
		prname = input("         > ")
		while not (os.path.exists("./config/" + prname + ".json")):
			print("not a valid project")
			prname = input("        > ")

		resp = input("project is valid, do you want to generate it ( confirm by typing y?")

		if (resp=="y"):
			os.system("cp ./config/" + prname + ".json generators/config.json") 
			file = open("./generators/config.json","r+")
			json_data = json.load(file)
			type = json_data["type"]
			file.close()

			if (type == "C"):
				os.system("python ./generators/CGenerator.py")

			elif (type =="C++"):
				os.system("python ./generators/CppGenerator.py")

			elif (type == "Python"):
				os.system("python ./generators/PythonGenerator.py")


	else:
		print("wrong input")
