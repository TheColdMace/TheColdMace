import subprocess
import time
from datetime import date

readFile = open("README.md","r")
contents = []
for line in readFile:
	contents.append(line)
readFile.close()
	
for line in contents:
	print(line)
while True:
	current = str(date.today())
	if contents[3] != "Today's Date is: " + current:
		writeFile = open("README.md","w")
		contents[3] = "Today's Date is: " + current
		writeFile.write(contents[0])
		writeFile.write(contents[1])
		writeFile.write(contents[2])
		writeFile.write(contents[3])
		print(contents[3])
		writeFile.close()
		subprocess["git","add","README.md"]
		subprocess["git","commit","-m",'"Updated file date"']
		subprocess["git","push"]
	time.sleep(86400)