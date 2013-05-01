"""
   File to merge output data
"""   

#! /usr/bin/python -tt
import bs4
import sys
import os
import json
import copy
import shutil

def merge(directory,mfile_name):
	dict1={}
	filelist = os.listdir(directory)
	for file1 in filelist:
		f=open(directory+'/'+file1,'r')
		s=f.read()
		t=json.loads(s)
		f.close()
		for k in sorted(t.keys()):
			dict1[k]=t[k]
		dict2={}
		for k in sorted(dict1.keys()):
			dict2[k]=dict1[k]
		dict1=dict2
		dict2={}
	final=open(mfile_name,'w')
	json.dump(dict1,final)
	final.close()
	#for file1 in filelist:
	#	os.remove(directory+'/'+file1)
	#os.rmdir(directory)
	shutil.rmtree(directory)


def main():
	merge('./temp1','tag_data.txt')
	merge('./temp2','company_data.txt')
	merge('./temp3','position_data.txt')
	sys.exit(0)

if __name__ == '__main__':
	main()
