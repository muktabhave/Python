def AlternateMinMaxArray(a):
    
    i=1
    while (i<len(a)-1):
        
        if(a[i]<a[i-1]):
            
            a[i], a[i-1]= a[i-1], a[i]
    
        if((i+1)<len(a) and a[i]<a[i+1]):
        
            a[i], a[i+1]= a[i+1], a[i]
        
        i=i+2
    
    return a

if (__name__=="__main__"):
    
    print(AlternateMinMaxArray([1,2,3,4,5,6]))
