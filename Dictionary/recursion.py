def findfollowers(arr):
    
    for i in arr:
        
        if(type(i)==str):
            
            if(i in dict1):
                val=dict1.get(i)
                dict1[i]=val+1
            else:
                dict1[i]=0
        else:
            findfollowers(i)


if (__name__=="__main__"):
    
    a=[['a'], [['a', ['a']]], 'a']
    
    dict1=dict()
    
    findfollowers(a)
    
    for k,v in dict1.items():
        
        print(k,v)
