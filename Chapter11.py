#Regular Expressions

#Regex or Regexp
# very powerful and quite cryptic
import re
#re.search()
#find()
#re.findall()

def um():
	hand = open('mbox-short.txt')
	for line in hand:
		line = line.rstrip()
		if line.find('From:') >= 0:
			print(line)


def dois():

	hand = open('mbox-short.txt')
	for line in hand:
		line = line.rstrip()
		if re.search('^From:', line):
			print(line)



# ^X.* -> ^ match the start of the line 
#-> . match any caracter -> * many times 

#^X-\S+: -> ^ match the start of the line
# x- -> match any non-whitespace character
# + one or more times

#re.search() -> returnes true/false dependinf on whether the string matches the regular expression
# If we actually want the matching strings to be extracted, we use re.findall()

x = 'My 2 fAvorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
z = re.findall('[AEIOU]+', x)

#print(y)
#print(z)

#Greedy Matching -> the repeat characters(* and +) push outward in
# both directions (greedy) to match the largest possible string

a = 'From: Using the : character'
b = re.findall('^F.+:', a)
#print(b)

# ^F -> first character in the match is an F
# .+ one or more characters
# : last character in the match is a :



def nongreedymatching():
#Non-Greedy Matching -> Not all regular expression repeat codes are greedy!
#If you add a ? character, the + and * chill out a bit ...
	x = 'From: Using the : character'
	y = re.findall('^F.+?:', x)
	print(y)

# ^F -> first character in the match is an F
# .+? -> one more characters but not greedy
# : -> last character in the match is a :

#nongreedymatching()

def finetuningstringextraction():
	x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
	y = re.findall('\S+@\S+', x) #substituind por '.', retorna toda a string sem espaços
	print(y)
	# \S+@\S+ -> means at least one non-whitespace character

#finetuningstringextraction()	

def regExC():
	data = x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
	atpos = data.find('@')
	print(atpos)

	sppos = data.find(' ', atpos)
	print(sppos)

	host = data[atpos+1 : sppos]
	print(host)

#regExC()

def doublesplitpattern():
	line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
	words = line.split()
	email = words[1]
	pieces = email.split('@')
	print(pieces[1])

doublesplitpattern()

def regexversion_doublesplitpattern():
	lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
	y = re.findall('@([^ ]*)', lin)
	# [^ ] -> match non-blank character
	# * -> match many of them
	z = re.findall('From .*@([^ ]*)', lin)
	#^From -> starting at the beginning of the line, look for the string 'From'
	print(y)
	print(z)

#regexversion_doublesplitpattern()

def spamconfidence():
	hand = open('mbox-short.txt')
	numlist = list()
	for line in hand:
		line = line.rstrip()
		stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
		if len(stuff) != 1 : continue
		num = float(stuff[0])
		numlist.append(num)
	print('Maximum:', max(numlist))	


#spamconfidence() não deu certo

def escapecharacter():
	x = 'We just received $10.00 for cookies'
	y = re.findall('\$[0-9.]+', x)
	# \$ -> a real dollar sign
	# A digit or period -> [0-9.]
	# + -> as least one or more 
	print(y)

escapecharacter()	
