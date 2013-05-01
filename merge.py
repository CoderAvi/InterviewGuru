"""
   Program to merge output files
   
"""   

#! /usr/bin/python -tt
import bs4
import sys
import os
import json
import copy
import shutil


def main():
    """
    list = [10 , 20 , 30 , 36]
    total_cluster_list = []
    
    for j in list:
        filename = 'Cluster2' + str(j) + '.txt' 
        f=open(filename,'r')
        s=f.read()
        tmplist=json.loads(s)    
        f.close()
        total_cluster_list.extend(tmplist)
        
        with open('total_cluster.txt', 'w') as outfile:
                   json.dump(total_cluster_list, outfile)    
    """
    f=open('Cluster_1_company.txt','r')
    s=f.read()
    old_dict =json.loads(s)    
    f.close()
    f=open('overlap3_all.txt','r')
    s=f.read()
    add_dict =json.loads(s)    
    f.close()
    
    old_dict['all'] = add_dict['all']
        
    with open('cluster_1_total.txt', 'w') as outfile:
         json.dump(old_dict, outfile)     
















if __name__ == '__main__':
    main()