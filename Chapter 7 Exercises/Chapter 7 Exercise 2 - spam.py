#Gets the name of the file
fname = input('Enter the file name: ')

#Tries to open the file and if it fails kills the program
try:
	fhand = open(fname)
except:
	print("File cannot be opened: ", fname)
	exit()

#Starts up some required variables
count = 0
sum = 0.0

#If a line starts with X_DSPAM... it will add the float to sum and add 1 to count
for line in fhand:
	if line.startswith("X-DSPAM-Confidence: "):
		num = float(line[21:])
		sum += num
		count += 1

#Calculates average and prints it
average = sum / count
print("Average spam confidence: ", average)