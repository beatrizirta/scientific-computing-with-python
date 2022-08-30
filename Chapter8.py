def parteA():

	friends = ['Joseph', 'Glenn', 'Sally']
	for friends in friends:
		print('Happy New Year', friends)
	print('Done')


	z = ['Joseph', 'Glenn', 'Sally']
	for x in z:
		print('Happy New Year', x)
	print('Done!')


	friends = ['Joseph', 'Glenn', 'Sally']
	print(friends[1])

	fruit = 'Banana'
	#fruit[0] = 'B'

	x = fruit.lower()
	print(x)

	lotto = [2,14,26,41,63]
	print(lotto)
	#[2,14,26,41,63]

	lotto[2] = 28
	print(lotto)
	#[2,14,28,41,63]

	greet = 'Hello Bob'
	print(len(greet))
	#9
	x = [1,2,'joe', 99]
	print(len(x))
	#4

	print(range(4))

	friends = ['Joseph', 'Glenn', 'Sally']
	print(len(friends))
	#3
	print(range(len(friends)))


	for i in range(len(friends)):
		friend = friends[i]
		print('Happy New Year', friend)


	a = [1, 2, 3]
	b = [4, 5, 6]

	c = a + b

	print(c)

	t = [9, 41, 12, 3, 74, 15]
	print(t[1:3])
	print(t[:4])
	print(t[3:])
	print(t[:])

	x = list()
	type(x)
	dir(x)

def parteB():
	
	stuff = list()
	stuff.append('book')
	stuff.append(99)
	print(stuff)

	stuff.append('cookie')

	print(stuff)

	some = [1, 9, 21, 10, 16]
	print(9 in some)
	print(15 in some)
	print(20 not in some)

	friends = ['Joseph', 'Glenn', 'Sally']
	friends.sort()
	print(friends)

#parteB()


def numeros():
	nums = [3, 41, 12, 9, 74, 15]
	print(len(nums))
	print(max(nums))
	print(min(nums))
	print(sum(nums))
	print(sum(nums)/len(nums))

#numeros()	

def average():

	total = 0
	count = 0
	while True:
		inp = input('Enter a number: ')
		if inp == 'done' : break
		value = float(inp)
		total = total + value
		count = count + 1

	average = total / count
	print('Average:', average)


#average()	

def numlist():
	numlist = list()
	while True:
		inp = input('Enter a number: ')
		if inp == 'done' : break
		value = float(inp)
		numlist.append(value)
	average = sum(numlist)/len(numlist)
	print('Average:', average)

#numlist()

def parteC():
	abc = 'With three words'
	stuff = abc.split()
	#split breaks a string into parts and
	#produces a list of strings
	print(stuff)
	print(len(stuff))
	print(stuff[0])
	for w in stuff:
		print(w)

#parteC()

def parteD():

	line = 'A lot         of spaces'
	etc = line.split()
	print(etc)

	line = 'first;second;third'
	thing = line.split()
	print(thing)
	print(len(thing))

	thing = line.split(';')
	print(thing)
	print(len(thing))
#parteD()

def parteE():
	fhand = open('mbox-short.txt')
	for line in fhand:
		line = line.rstrip() #takes off the end of the new lines
		if not line.startswith('From ') : continue
		words = line.split()
		print(words[2])
		#base-levantamento-csv

		email = words[1]
		pieces = email.split('@')
		print(pieces[1])
parteE()