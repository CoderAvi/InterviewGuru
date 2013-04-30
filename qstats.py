#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import copy

def main():
	
	f=open('tag_data.txt','r')
	s=f.read()
	tag_dict=json.loads(s)
	f.close()
	print 'total question base size:',
	print len(tag_dict.keys())
	f=open('company_data.txt','r')
	s=f.read()
	company_dict=json.loads(s)
	f.close()
	sfile=open('stats.txt','w')
	tag_master={}
	company_list=[]
	for q in tag_dict.keys():
		tags=tag_dict[q]
		if len(tags)==0:
			if 'untagged' in tag_master:
				stats=tag_master['untagged']
			else:
				stats={}
				tag_master['untagged']=stats
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
		sfile.write('**************')
		sfile.write(c)
		sfile.write('**************\n')
		total=0
		for t in tag_master.keys():
			stats=tag_master[t]
			if c in stats:
				sfile.write(t+': '+str(stats[c])+'\n')
				total+=stats[c]
		sfile.write('TOTAL: '+str(total)+'\n')
	u_dict=tag_master['untagged']
	untagged_total=0
	for k in u_dict.keys():
		untagged_total+=u_dict[k]
	sfile.write('TOTAL UNTAGGED SIZE: '+str(untagged_total))

if __name__ == '__main__':
  main()

