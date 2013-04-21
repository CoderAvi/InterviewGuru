#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import copy

def main:
	f=open('tdata.txt','r')
	s=f.read()
	tag_dict=json.loads(s)
	f=open('cdata.txt','r')
	s=f.read()
	company_dict=json.loads(s)
	tag_master={}
	company_list=[]
	for q in tag_dict.keys():
		tags=tag_dict[q]
		for t in tags:
			if t in tag_master:
				stats=tag_master[t]
			else:
				stats={}
				tag_master[t]=stats
		company=company_dict[q]
		if company not in company_list:
			company_list.append(company)
		if company in stats:
			stats[company]=stats[company]+1
		else:
			stats[company]=1
	for c in company_list:
		print 'company name: ',c
		total=0
		for t in tag_master.keys():
			stats=tag_master[t]
			if c in stats:
				print 'tag ',t,': ',stats[c],' ',
				total+=stats[c]
		print 'total: ',total

if __name__ == '__main__':
  main()

