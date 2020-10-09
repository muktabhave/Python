def ismonotonic(a):
    
    increasing= False
    decreasing= False
    
    for i in range (0, len(a)-1):
        
        if(a[i]> a[i+1]):
            
            decreasing= True
            
        if (a[i]< a[i+1]):
            
            increasing= True
    
    if (decreasing== True and increasing==True):
        
        return True
    
    return False
    
    
if (__name__=="__main__"):
    
    print(ismonotonic([1,2,8,2]))
