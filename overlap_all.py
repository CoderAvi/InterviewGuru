#!/usr/bin/python -tt
import bs4
import sys
import os
import json
import math


def find_sim(vector,v1,v2):
    tmp1 = vector[v1]
    tmp2 = vector[v2]
   
    dotpdt = 0
    for i in range(len(tmp1)):
        dotpdt += tmp1[i] * tmp2[i]

    return dotpdt    
        
    


def do_cluster(vector,clist):
    
    f=open('question_data.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    
    threshold = 4
    i = 1
    cluster = {}
    return_list = []
    clist1 = clist * 1
    tmplist = clist * 1
    
    while len(tmplist) > 0:
     for v1 in clist1:
        cluster[i] = []
        cluster[i].append(v1)
        if v1 in tmplist:
          tmplist.remove(v1)
        clist2 = tmplist * 1
        for v2 in clist2:
            if(find_sim(vector,v1,v2) >= threshold):
                #print find_sim(vector,v1,v2)
                cluster[i].append(v2)
                tmplist.remove(v2)
        i += 1
        
    #print "no of clusters is " , i 
    for key in cluster.keys():
        tmp = cluster[key]
        if len(tmp) > 1:
            return_list.append(tmp)
           
    return return_list    
        
              
                
                
            
        

def main():
    
    f=open('new_vector_data.txt','r')
    s=f.read()
    vector=json.loads(s)    
    f.close()
    
    f=open('company_data.txt','r')
    s=f.read()
    company=json.loads(s)    
    f.close()
    
    f=open('fullytagged_data.txt','r')
    s=f.read()
    tag_data=json.loads(s)    
    f.close()
    
    f=open('question_data.txt','r')
    s=f.read()
    qn_dict=json.loads(s)    
    f.close()
    
    
   
       
    
    
    cluster_dict = {}
    cluster_dict['all'] = {}
    qn_list = []
    for key in company.keys():
         qn_list.append(key)    
    #categorize them by the tags        
    tag_dict = {}        
    for qn in qn_list:
        tag_list = tag_data[qn]
        for tag in tag_list:
            if tag in tag_dict:
                tag_dict[tag].append(qn)
            else:
                tag_dict[tag] = []
                tag_dict[tag].append(qn)
                  
    
    for tag in tag_dict.keys():
        clist = tag_dict[tag]
        if len(clist) > 20 :
           cluster_list = do_cluster(vector,clist)
           tmplist1 = []
           for list in cluster_list:
               tmplist2 = []
               for qn in list:
                   tmp = qn + ":::" + qn_dict[qn]
                   tmplist2.append(tmp)
               tmplist1.append(tmplist2)   
           cluster_dict['all'][tag] = tmplist1
           
    
           
   
            
    with open('all_cluster.txt', 'w') as outfile:
       json.dump(cluster_dict, outfile)
    print "Done"        

                        

if __name__ == '__main__':
  main()