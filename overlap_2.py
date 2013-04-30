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
    
    """
    #finding the list of companies
    company_list = []
    for key in company.keys():
        if company[key] not in company_list:
            company_list.append(company[key])
    """
    company_list = [ u'Amazon', u'Bloomberg LP', u'Facebook', u'Microsoft', u'Adobe', u'Yahoo', u'Google', u'Qualcomm', u'NVIDIA']

    #print company_list
           
      
    company_qn_dict = {}
    for comp in company_list:
        company_qn_dict[comp] = []
     #adding the question list to the companies
    for key in company.keys():
        if company[key] in company_qn_dict:
           company_qn_dict[company[key]].append(key)
                
    company_list1 = company_list * 1
    tmplist = company_list * 1   
    #initialising the dictionary for the companies
    company_qn_list = []
    for comp1 in company_list1:
       tmplist.remove(comp1)
       company_list2 = tmplist * 1
       for comp2 in company_list2:
         tmp_dict = {}
         tmp_dict['c1'] = comp1
         tmp_dict['c2'] = comp2
         company_qn_list.append(tmp_dict)

   
    cluster_list = []
    j = 0
    #for key in company_qn_dict.keys():
    for i in company_qn_list:
            tmpdict = {}
            comp1 = i['c1']
            comp2 = i['c2']
            tmpdict['c1'] = comp1
            tmpdict['c2'] = comp2
            tmpdict['data'] = {}
           
            qn_list = []
            
            qn_list1 = company_qn_dict[comp1] * 1
            qn_list2 = company_qn_dict[comp2] * 1
            qn_list.extend(qn_list1)
            qn_list.extend(qn_list2)
             
            #categorize them by the tags        
            tag_dict = {}        
            for qn in qn_list:
                tag_list = tag_data[qn] * 1
                for tag in tag_list:
                    if tag in tag_dict:
                        tag_dict[tag].append(qn)
                    else:
                        tag_dict[tag] = []
                        tag_dict[tag].append(qn)
             
            
            # qn part                       
            append = 0
            tempdict = {}
            for tag in tag_dict.keys():
                clist = tag_dict[tag] * 1
                if len(clist) > 20 :
                   append = 1 
                   clusted_list = do_cluster(vector,clist)
                   tmplist1 = []
                   for list in clusted_list:
                       tmplist2 = []
                       for qn in list:
                           tmp = qn + ":::" + qn_dict[qn]
                           tmplist2.append(tmp)
                       tmplist1.append(tmplist2)   
                   tempdict[tag] = tmplist1 
         
            j += 1
             
            print j
    
            tmpdict['data'] = tempdict
                   
            if append == 1:
               cluster_list.append(tmpdict)    
            
            """
            print tmpdict
            if j == 1:
                sys.exit(0)
            """
            
            if j % 10 == 0 or j ==  36:
                filename = 'Cluster2' + str(j) + '.txt'
                with open(filename, 'w') as outfile:
                   json.dump(cluster_list, outfile)
                cluter_list = []   
                
    print "Done"  
    
                         

if __name__ == '__main__':
  main()