#C:\Users\abfnd\Downloads
#handle = open(filename, mode)
#fhand = open('mbox.txt')
#print(mbox.txt)

xfile = open('base-levantamento-csv','r')
for cheese in xfile:
	print(cheese)

fhand = open('mbox.txt')
count = 0
for line in fhand:
	count = count + 1
print('Line Count:', count)

fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])


def pasta1():

	fhand = open('mbox-short.txt')
	for line in fhand:
	if line.startswith('From:'):
		print(line)


	fhand = open('mbox-short.txt')
	for line in fhand:
		line = line.rstrip()
		if line.startswith('From:'):
			print(line)


	fhand = open('mbox-short.txt')
	for line in fhand:
		line = line.rstrip()
		if not line.startswith('From:'):
			continue
		print(line)	

	fhand = open('mbox-short.txt')
		for line in fhand:
			line = line.rstrip()
			if not '@uct.ac.za' in line:
				continue
			print(line)


	fname = input('Enter the file name: ')
	fhand = open(fname)
	count = 0

	for line in fhand:
		if line.startswith('Subject:'):
			count = count + 1
		print('There were', count, 'subject lines in', fname)


	#BAD NAME FILES

	fname = input('Enter the file name: ')
	try:
		fhand = opne(fname)
	except:
		print('File cannot be opened:', fname)
		quit()

	count = 0
	for line in fhand:
		if line.startswith('Subject:') :
			count = count + 1
	print('There were', count, 'subject lines in', fname)	


