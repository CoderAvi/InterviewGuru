#! /usr/bin/python -tt
import bs4
import sys
import os
import json
import copy


def main():
	dict1={}
	filelist = os.listdir("/Users/Macho/Developer/IR/indices/")
	for file1 in filelist:
		f=open("/Users/Macho/Developer/IR/indices/"+file1,'r')
		s=f.read()
		t=json.loads(s)
		for k in sorted(t.keys()):
			dict1[k]=t[k]
		dict2={}
		for k in sorted(dict1.keys()):
			dict2[k]=dict1[k]
		dict1=dict2
		dict2={}
	final=open('dataf.txt','w')
	json.dump(dict1,final)
	sys.exit(0)

if __name__ == '__main__':
	main()
