INTERVIEW GURU:
===============


CRAWLING :
==========

- We crawled careercup.com. We give the ur for each page to crawl all the questions in that page. 
- The files corresponding to crawling are available in WebCrawler folder
- The crawled files are saved in user specified location. In order to change the location make changes to BasicCrawlController_Careercup.java and   BasicCrawler_Careercup.java
  

PARSING :
=========

- To parse the question content run parser_1.py . Change the location to the folder where the crawled files are available. The parsed data will be available
   in question_data.txt
- To parse the tags related to the question run parser_2.py . As mentioned above change the location. the parsed data will be available in company_data.txt- which contains the company info for each quesiton , position_data.txr - which contains the type of position for each question and tag_data.txt - which contains a list of tags for each question . 


RETAGGING :
===========

- Some of the original tags are not useful and many questions are untagged . Run tagging.py to retag the questions. The new tags will be available in   fullytagged_data.txt

VECTOR REPRESENTAION :
======================

- Each question is represented as a vector. Run featurerep.py to generate the vector file new_vector_data.txt. 


FINDING DISTRIBUTION :
======================

- ui_1.py is used to generate the distribution of focus area for each company

FINDING CLUSTERS :
=================

- overlap_1.py is used to find clusters of questions for each company. The clusters are stored in Cluster_1_company.txt
- overlap_2.py is used to find cluster of questions for combination of companies. The clusters are divided and saved in several files. They are later merged to total_cluster.txt
- overlap_all.py is used to find cluster of questions from all companies. The clusters are saved in all_cluster.txt
- merge.py is used to merge the output of overlap_1.py and overlap_all.py. The resultant file is cluster_1_total.txt


UI:
==