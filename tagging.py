#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import copy
import operator
import re
import math


def main():
    
    f=open('tag_data.txt','r')
    s=f.read()
    tag_dict=json.loads(s)    
    f.close()
    
    doc_dict = {}
    untagged_list = []
    
    for key in tag_dict.keys():
        tmplist = tag_dict[key]
        if len(tmplist) == 0:
             untagged_list.append(key)
        else:
         for i in tmplist:
            if i in doc_dict:
                doc_dict[i].append(key)
            else:
                doc_dict[i] = []
                doc_dict[i].append(key)


    """   
    doc_count = {}            
    for key in doc_dict.keys():
          doc_count[key] = len(doc_dict[key])          
            
    doc_prob = {}
    for key in doc_count.keys():
        doc_prob[key] = float(doc_count[key])/float(tag_count)
      
    from operator import itemgetter    
    list1 =  sorted(doc_count.items(),key=itemgetter(1),reverse=True)
    for i in list1:
        print i[0]
    for i in list1:
        print i[1]
    """
   
    f=open('qn.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    #Training 
   
    vocab = {}
    total = {}
    b = 0   
    tag_term_freq = {}
    
    for key in doc_dict.keys():
        tmp = {}
        doc_list = doc_dict[key]
        for doc in doc_list:
            string = qn_dict[doc]
            str1 = string.lower()
            words = re.findall(r'[a-z]+',str1)   
            for word in words:
              if word in tmp:
                 tmp[word] += 1
              else:
                 tmp[word] = 1
              if word in vocab:
                 continue
              else:
                 vocab[word] = 1
                 b += 1
        x = 0
        for i in tmp:
          x += tmp[i]
        total[key] = x   
        tag_term_freq[key] = tmp
        
    for key1 in tag_term_freq.keys():
       for key2 in tag_term_freq[key1]:
          tag_term_freq[key1][key2] = float(tag_term_freq[key1][key2] + 1)/float(total[key1] + b)
        
   
    
 #Testing
     
    for doc in untagged_list:
        if doc in qn_dict.keys():
          string = qn_dict[doc]
        else:
            continue  
        str1 = string.lower()
        words = re.findall(r'[a-z]+',str1)   
        maxval = -99999 
        maxclass = -1
        for tag in tag_term_freq.keys():
          x = 0 
          for word in words:
            if word in tag_term_freq[tag]:
               x += math.log10(tag_term_freq[tag][word])
            else:
               x += math.log10(float(1)/float(total[tag]+b))
          if x > maxval :
             maxval = x
             maxtag = tag
        tag_dict[doc].append(maxtag)
        
             
    for doc in untagged_list:
        print doc , tag_dict[doc]
    print len(untagged_list)












if __name__ == '__main__':
  main()
