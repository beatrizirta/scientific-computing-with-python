#Dictionaries {key: value}

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

#print(purse)
#print(purse['candy'])
purse['candy'] = purse['candy'] + 2
#print(purse)

def comparing():
	lst = list()
	lst.append(21)
	lst.append(183)
	print(lst)
	lst[0] = 23
	print(lst)

	ddd = dict()
	ddd['age'] = 21
	ddd['course'] = 182
	print(ddd)
	ddd['age'] = 23
	print(ddd)

#comparing()

def dictionaries():
	jjj = {'cuck' : 1, 'fred' : 42, 'jan': 100}
	print(jjj)
	ooo = { }
	print(ooo)

	ccc = dict()
	ccc['csev'] = 1
	ccc['cwen'] = 1
	print(ccc)
	ccc['cwen'] = ccc['cwen'] + 1
	print(ccc)

	counts = dict()
	names = {'csev', 'cwen', 'csev', 'zqian', 'cwen'}
	for name in names:
		if name not in counts:
			counts[name] = 1
		else:
			counts[name] = counts[name] + 1
	print(counts)

	
#dictionaries()

def dictionariesB():
	ccc = dict()
	ccc['csev'] = 1
	ccc['cwen'] = 1
	print(ccc)

	ccc['cwen'] = ccc['cwen'] + 1
	print(ccc)

	print('cse' in ccc)
	print('csev' in ccc)

#dictionariesB()

def dictionariesC():
	counts = dict()
	names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
	for name in names:
		if name not in counts:
			counts[name] = 1
		else:
			counts[name] = counts[name] + 1
		#print(counts)

	# or

	if name in counts:
		x = counts[name]
	else:
		x = 0
	# or

	x = counts.get(name, 0)

	# or

	counts = dict()
	names = ['csev', 'cwen', 'csev', 'zquian', 'cwen']
	for name in names:
		counts[name] = counts.get(name, 0) + 1
	print(counts)


#dictionariesC()

def CountingPattern():
	counts = dict()
	print('Enter a line of text:')
	line = input('')

	words = line.split()

	print('Words:' , qwords)

	print('Counting...')
	for word in words:
		counts[word] = counts.get(word, 0) + 1
	print('Counts', counts)	

#CountingPattern()

def ListofKeys():
	counts = {'chuck' : 1, 'fred' : 42, 'jan':100}
	for key in counts:
		print(key, counts[key])

#ListofKeys()

def listsofKeysandValues():
	jjj = {'chuck' : 1, 'fred': 42, 'jan': 100}
	print(list(jjj))

	print(jjj.keys())

	print(jjj.values())

	print(jjj.items())

#listsofKeysandValues()

def twoIterationVariables():
	jjj = { 'chuck' : 1, 'fred': 42, 'jan': 100}
	for aaa,bbb in jjj.items():
		print(aaa,bbb)
twoIterationVariables()

def dictionariesD():
	name = input('Enter file:')
	handle = open(name)
	
	counts = dict()
	for line in handle:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word,0) + 1

	bigcount = None
	bigword = None
	for word, count in counts.items():
		if bigcount is None or count > bigcount:
			bigword = word
			bigcount = count	
	
dictionariesD()		