#Tuples

x = ('Glenn', 'Sally', 'Joseph')
#print(x[2])

y = (1, 9, 2)
#print(y)
#print(max(y))

#Cannot do with tuples

x = (3,2,1)
#x.sort()
#x.append(5)
#x.reverse()

l = list()
#print(dir(1))

t = tuple() #are limited lists, used to
#make temporary variables
#print(dir(t))

def tuplesanddictionaries():
	d = dict()
	d['csev'] = 2
	d['cwen'] = 4
	for (k,v) in d.items():
		print(k, v)

	tups = d.items()
	
	print(tups)

#tuplesanddictionaries()

def tuplesanddictionaries2():
	d = dict()
	d['Beatriz'] = 1
	d['Andrade'] = 2
	for (a,b) in d.items():
		print(a,b)

	tup = d.items() #por que dá erro ????
	#porque tem que chamar o dicionário de 'D'
	print(tup)

#tuplesanddictionaries2()


def tuples_compare():
	print((0, 1, 2) < (5, 1, 2))

	(0, 1, 200000) < (0, 3, 4)

	('Jones', 'Sally') < ('Jones', 'Sam')

	print(('Jones', 'Sam') < ('Adams', 'Sally'))

#tuples_compare()

def sorting_lists_of_tuples():
	d = {'a':10, 'b':1, 'c':22}
	print(d.items())
	print(sorted(d.items()))

	t = sorted(d.items())
	for k,v in sorted(d.items()):
		print(k,v)
	#sorted is a built in function wich
	#takes a sequence as a parameter and returns
	#a sorted sequence

	tmp = list()
	for k, v in d.items():
		tmp.append((v,k))
	print(tmp)

	tmp = sorted(tmp, reverse = True)
	print(tmp)

	#another way to write things:
	print(sorted([(v,k) for k,v in d.items()]))	
	#print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
sorting_lists_of_tuples()

def fhand():
	fhand = open('romeo.txt')
	counts = dict()
	for line in fhand:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word, 0)  + 1

	lst = list()
	for key, val in counts.items():
		newtup = (val, key)
		lst.append(newtup)

	lst = sorted(lst, reverse=True)

	for val, key in lst[:10]:
		print(key, val)	

	

#fhand()


