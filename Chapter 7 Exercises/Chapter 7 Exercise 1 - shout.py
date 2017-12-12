#Gets the name of the file
fname = input('Enter the file name: ')

#Tries to open the file and if it fails kills the program
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()

#Takes each line of the file and makes it all uppercase
for line in fhand:
	line = line.upper()
	print(line)