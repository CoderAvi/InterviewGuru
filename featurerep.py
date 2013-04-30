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
    
    f=open('question_data.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    f = open('features.txt','r')
    s = f.read()
    feature_list = json.loads(s)
    f.close()
    
    f = open('stem_dict.txt','r')
    s = f.read()
    stem_dict = json.loads(s)
    f.close()
    
    vocab = []
    vocab.extend(feature_list)
    for key in stem_dict.keys():
        if stem_dict[key] in vocab:
            continue
        else:
            vocab.append(stem_dict[key])
            
    
    vector = {}
    for key in qn_dict.keys():
      string = qn_dict[key]
      str1 = string.lower()
      tmplist1 = re.findall(r'[a-z]+',str1)
      tmplist2 = []
      tmpvector = []
      
      for word in tmplist1:
          if word in stem_dict.keys():
              text = stem_dict[word]
          else:
              text = word
          tmplist2.append(text)  
                
      for word in vocab:
         if word in tmplist2:
              tmpvector.append(1)
         else:
              tmpvector.append(0)
      vector[key] = tmpvector         
          
     
                  
    
    with open('new_vector_data.txt', 'w') as outfile:
            json.dump(vector, outfile)            
           
    print "Done"          
                
        
        
   
    
    
    
    
if __name__ == '__main__':
  main()