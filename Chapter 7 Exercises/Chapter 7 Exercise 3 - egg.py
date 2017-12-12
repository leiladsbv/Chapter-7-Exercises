#Gets the name of the file
fname = input('Enter the file name: ')

#Code for easter egg where if they put in "na na boo boo" as the file name they get a message.
if fname == "na na boo boo":
	print("NA NA BOO BOO TO YOU - You have been punk'd!")

else:
	#Tries to open the file and if it fails kills the program
	try:
		fhand = open(fname)
	except:
		print("File cannot be opened: ", fname)
		exit()

	count = 0
	for line in fhand:
		count += 1

	print("There were ", count, "subject line in ", fname)