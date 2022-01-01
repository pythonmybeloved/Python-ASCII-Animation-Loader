import time
import os
os.system('cls')
filetyped = input("File name? ")
filename = str(filetyped)
try:
	file = open(filename,'r')
except:
	print('Something went wrong. Closing...')
	time.sleep(1)
	exit()
read = file.readlines()
os.system('cls')
print("Converting file.")
time.sleep(0.5)
os.system('cls')
print("Converting file..")
time.sleep(0.5)
os.system('cls')
print("Converting file...")
time.sleep(0.5)
os.system('cls')
while True:
	for l in read:
		if '/na/' in l:
			read.index('/na/\n')
			time.sleep(0.5)
			os.system('cls')
		else:
			if 'eoa' in l:
				time.sleep(0.5)
				os.system('cls')
			else:
				print(l)
	