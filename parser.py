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
    #print len(filelist)
    i = 0
    for file in filelist:
        print file  
        dict2 = {}
        filename = "C:\Users\sindhu\Desktop\ir\project\careercup\\" + file 
        f=open(filename)
        html=f.read()
        soup=bs4.BeautifulSoup(html)
        #qn = soup.body.find('span',attrs={'class':'entry'}).find('p').text
        tmp1 = soup.body.find('span',attrs={'class':'entry'})
        if tmp1 != None:
            tmp2 = tmp1.find('p')
            if tmp2 != None :
               qn = tmp1.text
               dict2['qn'] = qn
        tmp = soup.body.find('span',attrs={'class':'tags'}).find_all('a')
        """
        tags = ['company','position','type1','type2','type3','type3','type4','type5','type6','type7','type8','type9','type10','type11']
        j = 0
        for x in tmp:
            #print j
            dict2[tags[j]] = x.contents[0]
            j += 1
        """
        dict2['company'] = tmp[0].contents[0]
        if len(tmp) > 1:
         dict2['position'] = tmp[1].contents[0]
        tags = []
        j = 1
        for x in tmp:
            if j <= 2:
                j += 1
                continue
            tags.append(x.contents[0])
            
            
        dict2['tags'] = tags  
        dict1[i] = dict2
        #print dict2
        i += 1
        #if i == 5:
         #   sys.exit(0)

        
    with open('data.txt', 'w') as outfile:
        json.dump(dict1, outfile)
    sys.exit(0)
                
if __name__ == '__main__':
  main()
