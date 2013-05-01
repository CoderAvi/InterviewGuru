"""
  File to generate the distribution of different focus areas/tags 
  for each company.
  
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
    
    f=open('fullytagged_data.txt','r')
    s=f.read()
    tag_dict=json.loads(s)    
    f.close()
    
    f=open('question_data.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    f=open('company_data.txt','r')
    s=f.read()
    company_data=json.loads(s)
    f.close()
    
    company_dict = {}
    company_dict['all'] = []
    for key in company_data.keys():
        tmp = company_data[key]
        if tmp in company_dict:
            company_dict[tmp].append(key)
        else:
            company_dict[tmp] = []
            company_dict[tmp].append(key)
        company_dict['all'].append(key)    
            
    #print company_dict.items()
          
        

    dict1 = {}
    dict1['name'] = 'company stats'
    dict1['children'] = []
    
    for key in company_dict.keys():
        tmp = {}
        tmp['name'] = key
        tmp['children'] = []
        tmp2 = {}
        tmp2['name'] = 'distribution'
        dict2 = {}
        dict3 = {}
        
        tmp1 = company_dict[key]
        total = len(tmp1)
        
        for qn in tmp1:
            tag_list = tag_dict[qn]
            for tag in tag_list:
               if tag in dict2:
                  dict2[tag] += 1
               else:
                  dict2[tag] = 1
   
                  
        dict3[key] = []
        for tag in dict2.keys():
               tmpdict = {}
               tmpdict['name'] = tag
               tmpdict['size'] = dict2[tag]
               dict3[key].append(tmpdict)
        tmp2['children'] = dict3[key]            
        tmp['children'].append(tmp2)
        dict1['children'].append(tmp)
        
    with open('ui_1.txt', 'w') as outfile:
            json.dump(dict1, outfile)
        
            
    print "Done"      
   
    
             
                       
        
    
        
                        
                    
                    
            
            
       
















if __name__ == '__main__':
  main()