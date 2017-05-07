from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'http://christwire.org/'

conn = urlopen(url)
html = conn.read()

soup = BeautifulSoup(html)
links = soup.find_all('a')

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def hasPrefix(inputString):
	if url not in inputString:
		inputString = url + inputString
	return inputString

urls = set()

with open('fakenewsurl.txt', 'w') as output:
	for tag in links:
	    link = tag.get('href',None)
	    if link is not None:
	    	if hasNumbers(link) and link not in urls:
	    		output.write(hasPrefix(link) + '\n')
	    		urls.add(link)