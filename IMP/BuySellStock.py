def maxprofit(a):
    
    profit=0
    i=0
    l=[]
    n=len(a)-1
    
    if(len(a)==1):
        return 0
        
    while(i<n):
        
        while(i<n and a[i+1]< a[i]):
            
            i=i+1
        
        if (i==n-1):
            break
        
        buy=i
        buyval= a[i]
        
        i=i+1
        
        while(i<n and a[i]> a[i-1]):
            
            i=i+1
        
        sell=i-1
        sellval=a[i-1]
        
        l.append(buyval)
        l.append(sellval)
       
        
        profit=profit+ (sellval-buyval)

        
    return profit

if (__name__=="__main__"):
    
    print(maxprofit([7,1,5,3,6,4]))
