# Remove Kth character from strings list 

def removekthletter(s, k): 
    
    res=[]
    for ele in s:
        
        res.append(ele[:k]+ ele[k+1:])
        
    return res

if(__name__=="__main__"):
    
    test_list = ['akash', 'nikhil', 'manjeet', 'akshat'] 
    
    print(removekthletter(test_list, 2))
