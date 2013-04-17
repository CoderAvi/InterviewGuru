#!/usr/bin/python -tt
import bs4
import sys
import os
import json

#this file 
#this file contains the code snippet to parse HTML
def main():
	dict1 = {}
	filelist = os.listdir("C:\Users\sindhu\Desktop\ir\project\careercup")
	print len(filelist)
	i = 0
    for file in filelist:  
   	    dict2 = {}
		f=open(file)
		html=f.read()
		soup=bs4.BeautifulSoup(html)
		qn = soup.body.find('span',attrs={'class':'entry'}).find('p').text
		print qn
		dict2['qn'] = qn
		tmp = soup.body.find('span',attrs={'class':'tags'}).find_all('a')
		company = tmp[0].contents[0]
		position = tmp[1].contents[0]
		type =  tmp[2].contents[0]
	    dict2['company'] = company
	    dict2['position'] = position
	    dict2['type'] = type
		print company , position , type
		dict1[i] = dict2
		i += 1
	with open('data.txt', 'w') as outfile:
    json.dump(dict1, outfile)
	sys.exit(0)
				
if __name__ == '__main__':
  main()
