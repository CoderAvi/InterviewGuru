#! /usr/bin/python -tt
import bs4
import sys
import os
import json
import copy


def main():
	dict1={}
	filelist=os.listdir("/Users/Macho/Developer/IR/data/careercup/database")
	fileno=1
	ofno=0
	for file1 in filelist:
		print file1
		filename="/Users/Macho/Developer/IR/data/careercup/database/"+file1
		f=open(filename)
		html=f.read()
		f.close()
		soup=bs4.BeautifulSoup(html)
		tmp=soup.body
		if tmp==None:
			continue
		tmp=tmp.find('span',attrs={'class':'tags'})
		if tmp==None:
			continue
		tmp=tmp.find_all('a')
		#dict1[file1]=tmp.text
		tags=[]
		dict1[file1]=tags	
		if len(tmp)<=2:
			print 'c...'
			continue
		tmp=tmp[2:]
		for x in tmp:
			l=x.contents[0]
			#print l
			m=l[:]
			#m=copy.deepcopy(l)
			tags.append(l)
		soup=None
		fileno=fileno+1
		if fileno > 200:
			ofno=ofno+1
			outfile=open('data'+str(ofno)+'.txt','w')
			fileno=1
			json.dump(dict1,outfile)
			outfile.close()
			dict1={}
	outfile=open('data.txt','w')
	json.dump(dict1,outfile)
	sys.exit(0)

if __name__ == '__main__':
	main()
