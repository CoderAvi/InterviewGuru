#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import re
import math
import copy
import operator


def main():
    
    f=open('qn.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    f = open('words.txt','r')
    s = f.read()
    imp_words = json.loads(s)
    f.close()
    df = {}
    idf = {}
    gtf = {}
    vector = {}

    for key in qn_dict.keys():
      string = qn_dict[key]
      str1 = string.lower()
      words = []
      tmplist1 = re.findall(r'[a-z]+',str1)
      
      for word in tmplist1:
          if len(word) <= 3:
              if word in imp_words:
                words.append(word)
              else:
                continue
          else:
              words.append(word)
     
                  
      tf = {}
      for word in words:
          if word in tf:
             tf[word] += 1
          else:
             tf[word] = 1
      wtf = {}
      for key in tf.keys():
        wtf[key] = 1 + math.log10(tf[key])
      uwords = {}
      for word in words:
        if word in uwords:
           continue
        else:
           uwords[word] = 1
      for word in uwords:
        if word in df:
           df[word] += 1
        else:
           df[word] = 1
  
    filelist = os.listdir("C:\Users\sindhu\Desktop\ir\project\careercup")
    ndoc = len(filelist)
    for key in df:
      idf[key] = math.log10(float(ndoc) /float(df[key]))
      
    from operator import itemgetter  
    randlist = sorted(idf.items(),key=itemgetter(1),reverse=True)
    print len(randlist)
    #for i in randlist:
     #   print i
    
   
    
    
    
    
if __name__ == '__main__':
  main()