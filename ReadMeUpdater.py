#import subprocess
import time
from datetime import date

readFile = open("README.md","r")
contents = []
for line in readFile:
	contents.append(line.strip())
readFile.close()
writeFile = open("README.md","w")

	
for line in contents:
	print(line)
while True:
	if contents[3] != "Today's Date is: " + date.today():
		contents[2] = "Today's Date is: " + date.today()
		writeFile.write(contents[0])
		writeFile.write(contents[1])
		writeFile.write(contents[2])
		writeFile.write(contents[3])
	time.sleep(86400)