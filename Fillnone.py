def fillnone(a):
    
    for i in range (len(a)):
        
        if(a[i]==None):
            
            a[i]=a[i-1]
    
    return a

if (__name__=="__main__"):
    
    print(fillnone([1,None,2,3,None,None,5,None]))
    
