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
    
    vector = {}
    for key in qn_dict.keys():
      string = qn_dict[key]
      str1 = string.lower()
      tmplist = re.findall(r'[a-z]+',str1)
      tmpvector = []
      for word in feature_list:
         if word in tmplist:
              tmpvector.append(1)
         else:
              tmpvector.append(0)
      vector[key] = tmpvector         
          
     
                  
    
    with open('new_vector_data.txt', 'w') as outfile:
            json.dump(vector, outfile)            
           
    print "Done"          
                
        
        
   
    
    
    
    
if __name__ == '__main__':
  main()