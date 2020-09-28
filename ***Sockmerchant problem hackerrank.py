#Sockmerchant problem hackerrank
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    dict1={}
    
    count=0
    
    for ele in ar:
        
        if (ele in dict1.keys()):
            
            dict1[ele]=dict1.get(ele)+1

        else:
            dict1[ele]=1
    
    for i in dict1.values():  
        
        if (i>1):
            count=count+(math.floor(i/2))
    
    return (count)
