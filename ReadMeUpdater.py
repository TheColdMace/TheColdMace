#import subprocess

readFile = open("README.md","r")
#writeFile = open("README.md","w")
string = ""
for line in readFile:
	string = string + line
	
print(string)