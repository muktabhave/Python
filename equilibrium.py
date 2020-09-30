#equilibrium is the index in array who has sum of its left side elements equal to sum of its right side elements

def equilibrium(a):
    
    n= len(a)
    leftsum=[0]*n
    
    for i in range (1,n):
        leftsum[i]=a[i-1]+leftsum[i-1]
    
    rightsum=[0]*n
    
    i=n-2
    
    while(i>=0):
        rightsum[i]=rightsum[i+1]+a[i+1]
        
        if (rightsum[i]==leftsum[i]):
            return i
        
        i=i-1
    
    return "not found"

if (__name__=="__main__"):
    
    print(equilibrium([10,20,10,-30,60]))
