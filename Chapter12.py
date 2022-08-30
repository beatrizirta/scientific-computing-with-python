# HTTP - Hypertext transfer protocol
# Protocol - http://
# Host - www.dr-chuck.com
# Document - /page1.htm

# Let's Write a Web Browser
import socket

def newb_web_browser():
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('data.pr4e.org', 80))
	cms = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
	mysock.send(cms)

	while True:
		data = mysock.recv(512)
		if (len(data) < 1):
			break
		print(data.decode())
	mysock.close()


#print(ord('H')) -> 

# Python Strings to Bytes

def newb_web_browser1():
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('data.pr4e.org', 80))
	cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
	mysock.send(cmd)

	while True:
		data = mysock.recv(512)
		if (len(data) < 1):
			break
		print(data.decode())
	mysock.close()


def newb_web_browser2():
	import urllib.request, urllib.parse, urllib.error

	fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
	for line in fhand:
		print(line.decode().strip())
		

#newb_web_browser2()

def newb_web_browser3():
	import urllib.request, urllib.parse, urllib.error

	fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
	counts = dict()
	for line in fhand:
		words = line.decode().strip()
		for word in words:
			counts[word] = counts.get(word, 0) + 1
	print(counts)

newb_web_browser3()

def Read_web_pages():

	import urllib.request, urllib.parse, urllib.error

	fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
	for line in fhand:
		print(line.decode().strip())


#Read_web_pages()


def web_scrapping():

	import urllib.request, urllib.parse, urllib.error
	from bs4 import BeautifulSoup

	url = input('Enter - ')
	html = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tags = soup('a')
	for tag in tags:
		print(tag.get('href', None))	

web_scrapping()