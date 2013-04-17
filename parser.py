#!/usr/bin/python -tt
import bs4
import sys

#this file 
#this file contains the code snippet to parse HTML
def main():
	f=open("/Users/Macho/Developer/IR/sample2.html")
	html=f.read()
	soup=bs4.BeautifulSoup(html)
	print soup.body.find('span',attrs={'class':'entry'}).find('p').text
	sys.exit(0)
				
if __name__ == '__main__':
  main()
