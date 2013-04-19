#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import copy

#this file 
#this file contains the code snippet to parse HTML
def main():
    dict1 = {}
    #question=[]
    #filelist = os.listdir("C:\Users\sindhu\Desktop\ir\project\careercup")
    filelist = os.listdir("/Users/Macho/Developer/IR/data/careercup/database")
    #print len(filelist)
    i = 0
    for file1 in filelist:
        print file1  
        #dict2 = {}
        #filename = "C:\Users\sindhu\Desktop\ir\project\careercup\\" + file 
        filename = "/Users/Macho/Developer/IR/data/careercup/database/"+file1
        f=open(filename)
        html=f.read()
        f.close()
        soup=bs4.BeautifulSoup(html)
        #qn = soup.body.find('span',attrs={'class':'entry'}).find('p').text
        '''tmp1 = soup.body
        if tmp1 !=None:
        	tmp1=tmp1.find('span',attrs={'class':'entry'})
        if tmp1 != None:
            tmp2 = tmp1.find('p')
            if tmp2 != None :
               qn = tmp2.text
               dict1[file1]=qn
               #dict2['qn'] = qn
        soup=None
        '''
        tmp = soup.body
       	if tmp == None:
       	    continue
        tmp=tmp.find('span',attrs={'class':'tags'})
        if tmp == None:
            continue
        tmp=tmp.find_all('a')
        tags = []
        dict1[file1] = tags
        if len(tmp)<=2:
            continue
        tmp=tmp[2:]
        for x in tmp:
				    tags.append(x.contents[0]) 
				soup=None
    with open('data.txt', 'w') as outfile:
		    json.dump(dict1, outfile)
    sys.exit(0)        
if __name__ == '__main__':
  main()
  
  
'''  
  					#l=x.contents[0]
					#m=copy.deepcopy(l)
        #print tmp
        #sys.exit(0)
        #dict2['company'] = tmp[0].contents[0]
        #if len(tmp) > 1:
        # dict2['position'] = tmp[1].contents[0]
					




'''
