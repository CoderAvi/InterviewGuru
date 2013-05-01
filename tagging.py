""" 
  File to retag the questions
  
"""  

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
    tag_dict_old=json.loads(s)    
    f.close()
    
    f=open('retagging.txt','r')
    s=f.read()
    retagging=json.loads(s)    
    f.close()
    
    doc_dict = {}
    untagged_list = []
    tag_dict = {}
    
    # some of the existing tags are removed and some tags are reclassified
    for key in tag_dict_old.keys():
        tmplist1 = tag_dict_old[key]
        tmplist2 = []
        if len(tmplist1) > 0:
            for tag in tmplist1:
                if tag == 'Algorithm':
                    continue
                elif tag == 'Coding':
                    continue
                elif tag == 'General Questions and Comments':
                    continue
                elif tag == 'Software Engineer / Developer':
                    continue
                elif tag == 'Ideas':
                    continue
                elif tag == 'Data Structures':
                    continue
                elif tag == 'Dynamic Programming':
                    continue
                elif tag == 'Sorting':
                    continue
                elif tag in retagging.keys():
                    newtag = retagging[tag]
                else:
                    newtag = tag
                  
                tmplist2.append(newtag)
        tag_dict[key] = tmplist2               
            
    
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


    
    doc_count = {}            
    total = 0
    for key in doc_dict.keys():
          doc_count[key] = len(doc_dict[key])
          total += len(doc_dict[key])          
            
    doc_prob = {}
    for key in doc_count.keys():
        doc_prob[key] = float(doc_count[key])/float(total)

       
    #Using Naive-Bayes to retag the untagged questions 
    f=open('question_data.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    #Training - our training data is tagged questions
   
    vocab = {}
    total = {}
    b = 0   
    tag_term_freq = {}
    
    for key in doc_dict.keys():
        tmp = {}
        doc_list = doc_dict[key]
        for doc in doc_list:
            if doc in qn_dict:
               string = qn_dict[doc]
            else:
                continue   
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
        
   
    
 #Testing - our testing data is the set of questions which are untagged
     
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
          x += math.log10(doc_prob[tag])     
          if x > maxval :
             maxval = x
             maxtag = tag
        tag_dict[doc].append(maxtag)
        
             
    for doc in untagged_list:
        print doc , tag_dict[doc]
    #print len(untagged_list)
    
    

    
    with open('fullytagged_data.txt', 'w') as outfile:
            json.dump(tag_dict, outfile)
    print "Done"        












if __name__ == '__main__':
  main()
